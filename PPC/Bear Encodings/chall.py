SOURCE = 'catctf{ENcODInG_4nD_eNcOdIN6s}'

from os import environ

if 'GZCTF_FLAG' in environ:
    SOURCE = environ['GZCTF_FLAG']

from base64 import b64encode, b32encode, b16encode
import codecs

def base16(s: str) -> str:
    return b16encode(s.encode()).decode()

def base32(s: str) -> str:
    return b32encode(s.encode()).decode()

def base64(s: str) -> str:
    return b64encode(s.encode()).decode()

def rot13(s: str) -> str:
    return codecs.encode(s, 'rot_13')


ENC_FUNCTIONS = [base16, base32, base64, rot13]

import random

seed = random.randint(0, 1000000)
random.seed(seed)

result = SOURCE

for i in range(30):
    function = random.choice(ENC_FUNCTIONS)
    result = 'ftctac{' + function(result) + '}'

with open('encodings.txt', 'w', encoding='utf-8') as f:
    f.write(str(seed) + '\n')
    f.write(result)

from http.server import test, SimpleHTTPRequestHandler

# run http server to host the file
test(SimpleHTTPRequestHandler, bind='0.0.0.0', port=8000)