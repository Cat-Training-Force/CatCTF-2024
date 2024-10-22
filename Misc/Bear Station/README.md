# Bear Station

熊老师约学生吃饭，发消息曰：我在车站等你们，并在群里附上了车站上拍的照片。

你看到了熊老师发的照片，于是你决定要一起去吃。找到车站的名称，用下面的 Python 脚本计算 flag.

```python
import re
from hashlib import sha256

def bear_hash(s: str):
    h = sha256(b"bear_bear{" + s.encode() + b"}")
    return h.hexdigest()

station = input("Station: ")
assert re.fullmatch("[A-Z][a-z]+", station)
ret = station
n = 0
for i in range(10676471):
    ret = bear_hash(ret)
print(f"catctf{{{ret}}}")
```
