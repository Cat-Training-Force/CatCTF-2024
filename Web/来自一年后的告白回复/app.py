import os
import random
import json
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for, flash, session, after_this_request
from werkzeug.utils import secure_filename
from sign import decrypt, encrypt, int_to_bytes
import pickle
import secrets
import string
import base64
import pickletools


def generate_random_string(length=32):
    alphabet = string.ascii_letters + string.digits  # 包含大小写字母和数字
    return ''.join(secrets.choice(alphabet) for _ in range(length))


flag = os.getenv('GZCTF_FLAG')
app = Flask(__name__)
app.config['SECRET_KEY'] = generate_random_string()
app.config['CONFIG_DIR'] = '/app/uploads'


# 初始化玩家状态
session = {
    "data": {
        'username': "nemo",
        'win_streak': 0,
        'highest_streak': 0
    }
}


def safe_load_data(record: bytes):
    black_list = ['os', 'sys', 'popen', 'system',
                  'eval', 'V', 'x', 'class', 'global', 'init', 'module']
    pickletools.dis(record)
    for i in black_list:
        if i.encode() in record:
            return None
    return pickle.loads(record)


# 处理玩家选择石头、剪刀、布
def play_game(player_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = determine_winner(player_choice, computer_choice)
    return computer_choice, result


# 判断胜负
def determine_winner(player, computer):
    if player == computer:
        return 'draw'
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return 'win'
    else:
        return 'lose'


# 首页路由
@app.route("/", methods=['GET', 'POST'])
def index():
    return redirect(url_for('game'))


# 游戏逻辑
@app.route("/game", methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        player_choice = request.form['choice']
        computer_choice, result = play_game(player_choice)

        if result == 'win':
            session['data']['win_streak'] += 1
            if session['data']['win_streak'] > session['data']['highest_streak']:
                session['data']['highest_streak'] = session['data']['win_streak']
            if session['data']['highest_streak'] >= 999 and session['data']['highest_streak'] < 999:
                return jsonify({'flag': flag})
        elif result == 'lose':
            session['data']['win_streak'] = 0

        return render_template('game.html', player_choice=player_choice, computer_choice=computer_choice, result=result, player_data=session['data'])

    return render_template('game.html', player_data=session['data'])


# 下载游戏记录
@app.route('/download', methods=['GET'])
def download():
    filename = f'{session['data']["username"]}_game_data'
    filepath = os.path.join(app.config['CONFIG_DIR'], filename)
    print(filepath)
    with open(filepath, 'wb') as fout:
        record = encrypt(pickle.dumps(session['data']))
        print(pickle.dumps(session['data']))
        fout.write(record)

    @after_this_request
    def remove_file(response):
        try:
            os.remove(filepath)
        except Exception as error:
            app.logger.error(
                f"Error removing or closing downloaded file handle: {error}")
        return response

    return send_file(filepath, as_attachment=True)


# 上传游戏记录
@app.route('/upload', methods=['POST'])
def upload_json():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['CONFIG_DIR'], filename)
        file.save(filepath)
        with open(filepath, 'rb') as fout:
            record = decrypt(fout.read())
            data_ins = safe_load_data((record))
            if data_ins != None:
                session['data'].update(data_ins)

            assert session['data']['username'] == 'nemo'
            assert isinstance(session['data']['win_streak'], int)
            assert isinstance(session['data']['highest_streak'], int)

        os.remove(filepath)
        return render_template('game.html', player_data=session['data'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
