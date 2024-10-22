from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import random
from utils import send_verification_code
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import string
import random
import hashlib
import os


def get_random_32bytes():
    s1 = ''.join(
        random.sample(string.ascii_letters+string.digits, 32))
    return hashlib.md5(s1.encode()).hexdigest()


app = Flask(__name__)
app.config['SECRET_KEY'] = get_random_32bytes()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# 定义用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True, nullable=False)
    secret = db.Column(db.String(100))
    password = db.Column(db.String(100), nullable=False)


# 创建数据库
with app.app_context():
    db.create_all()
    # 检查数据库是否已经存在数据
    if not User.query.first():
        # 初始化用户数据
        initial_users = [
            User(email='cattrainingforce@tongji.edu.cn',
                 secret=os.getenv('GZCTF_FLAG'),
                 password=generate_password_hash(get_random_32bytes())),
        ]
        db.session.bulk_save_objects(initial_users)
        db.session.commit()
        print("Initialized the database with default users.")


# 注册接口
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    secret = data.get('secret')
    password = data.get('password')

    # 检查邮箱或ID是否已存在
    existing_user = User.query.filter(
        (User.email == email)).first()
    if existing_user:
        return jsonify({'success': False, 'message': 'Email already exists.'})

    # 创建新用户并存入数据库
    hashed_password = generate_password_hash(password)
    new_user = User(email=email, password=hashed_password,
                    secret=secret)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Registration successful.'})


# 注册接口
@app.route('/register', methods=['GET'])
def register_render():
    return render_template('register.html')


# 处理发送验证码的AJAX请求
@app.route('/send_code', methods=['POST'])
def send_code():
    email = request.get_json().get('email')
    print("email", email)
    user = User.query.filter_by(email=email).first()
    # print(user.secret)

    if user:
        verification_code = ''.join(
            random.sample(string.ascii_letters+string.digits, 32))
        session['code'] = hashlib.md5(
            str(verification_code).encode()).hexdigest()
        session['error'] = 0

        send_verification_code(email, verification_code)  # 发送验证码
        return jsonify({'message': 'Verification code sent!', 'success': True})
    else:
        return jsonify({'message': 'Email not found!', 'success': False}), 404


# 默认接口
@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('login'))


# 登录页面
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        verification_code = request.form.get('verification_code')
        login_method = request.form.get('login_method')
        user = User.query.filter_by(email=email).first()

        if not user:
            flash('User does not exist.')
            return redirect(url_for('login'))

        if login_method == 'password':
            # 使用密码登录
            if user.password and check_password_hash(user.password, password):
                session['email'] = email
                session['logged_in'] = True
                return redirect(url_for('profile'))
            else:
                flash('Invalid password.')
                return redirect(url_for('login'))

        elif login_method == 'verification_code':
            if session.get('error') >= 5:
                flash(f'验证码失败次数达到上限，请重新申请验证码')
            else:
                # 使用验证码登录
                if session.get('code') == hashlib.md5(verification_code.encode()).hexdigest():
                    session['email'] = email
                    session['logged_in'] = True
                    return redirect(url_for('profile'))
                else:
                    session['error'] += 1
                    flash(f'验证码错误，失败{session.get('error')}次')
                    return redirect(url_for('login'))

    return render_template('login.html')


# 个人信息页面
@app.route('/profile')
def profile():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    email = session.get('email')
    user = User.query.filter_by(email=email).first()
    return render_template('profile.html', email=email, secret=user.secret)


# 退出登录
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
