import requests
from time import sleep
import re
import base64
import hashlib


url = "http://127.0.0.1/"
times = 0
session = requests.session()
data = {
    "answer":""
}
r = ""
while True:
    print("times=",times)
    if(times == 0):
        r = session.get(url=url,)

    pattern = r'\d+ [+\-x÷] \d+'
    try:
        s = re.search(pattern, r.text).group()
        if('+' in s):
            data['answer'] = eval(s)
        elif('-' in s):
            data['answer'] = eval(s)
        elif('x' in s):
            data['answer'] = eval(s.replace('x','*'))
        elif('÷' in s):
            data['answer'] = round(eval(s.replace('÷','/')))
        print(s)
        print(data['answer'])
    except:
        print(r.text)
    
    sleep(1.1)
    r = session.post(url=url,data=data,)
    print("--------------------------------------------------------------------")
    times += 1
    if('ctf' in r.text):
        print(r.text)
        break