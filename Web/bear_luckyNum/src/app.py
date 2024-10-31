from flask import Flask, render_template, request
from numpy.random import randint
import hashlib
import os

app = Flask(__name__)
flag = os.getenv("GZCTF_FLAG") if os.getenv("GZCTF_FLAG") is not None else "tjctf{Y0u_kn0w_h0w_t0_4ttack_we4k_passwd}"
luckyNum = randint(1,99999)
@app.route("/", methods=['POST', 'GET'])
def verify():
    if request.method == 'POST':
        # 获取JSON数据
        data = request.get_json()
        luckyNum_input = data.get('luckyNum')
        md5Val = data.get('md5Val')
            
        if luckyNum_input == str(luckyNum) and md5Val == hashlib.md5(str(luckyNum).encode('utf-8')).hexdigest():
            return flag
        else:
            return "你的幸运数字和熊老师不太一样哦~"
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run()