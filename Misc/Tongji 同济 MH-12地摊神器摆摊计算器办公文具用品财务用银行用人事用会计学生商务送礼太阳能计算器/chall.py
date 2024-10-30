BLACKLIST = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_=<>[]{}!@#$&|?\'"\\.'

def calc_(expression: str) -> str:
    try:
        result = eval(expression)
        if type(result) == bytes:
            result = result.decode()
        return result
    except:
        import traceback
        traceback.print_exc()
        return '无法计算，滚'


if __name__ == '__main__':
    from flask import Flask, jsonify, request, render_template
    from flask_cors import CORS, cross_origin

    app = Flask(__name__)
    cors = CORS(app)
    SECRET_LOCATION = '/chall/secret.txt'
    
    original_flag = open(SECRET_LOCATION).read().strip()
    print(original_flag)

    import os
    new_flag = os.environ.get('GZCTF_FLAG', original_flag)
    print(new_flag)

    open(SECRET_LOCATION, 'w').write(new_flag)

    from multiprocessing import Pool, TimeoutError

    def calc_dispatch(expression: str) -> str:
        for i in expression:
                if i in BLACKLIST:
                    return '黑客能不能爬'
        exe = calc_
        pool = Pool(processes=1)
        res = pool.apply_async(exe, kwds={'expression': expression})
        try:
            result = res.get(timeout=5)
        except TimeoutError:
            pool.terminate()
            pool.close()
            return '有人在瞎几把占用资源，举报了'
        result = str(result).strip()
        if result:
            return result
        else:
            return '无法计算，滚'

    @app.route('/calc', methods=['POST'])
    @cross_origin()
    def calc():
        expression = request.get_json()['expression']
        if expression.strip():
            return jsonify(result=calc_dispatch(expression))
        else:
            return jsonify(result='无法计算，滚')
        
    @app.route('/lk0.mp3', methods=['GET'])
    def lk0():
        return open('/lk0.mp3', 'rb').read()


    @app.route('/', methods=['GET'])
    def home():
        return render_template('frontend.html')

    app.run(host='0.0.0.0', port=1338)