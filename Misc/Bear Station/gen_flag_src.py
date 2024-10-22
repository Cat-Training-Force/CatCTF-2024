import re
import time
from hashlib import sha256


def bear_hash(s: str):
    h = sha256(b"bear_bear{" + s.encode() + b"}")
    return h.hexdigest()


station = "Kunsthaus"
assert re.fullmatch("[A-Z][a-z]+", station)
ret = station
n = 0
t0 = time.time()
while True:
    n += 1
    ret = bear_hash(ret)
    if ret.startswith("bea1bea2"):
        break
t1 = time.time()
print(n)
print(f"{(t1-t0) / 60:.2f}")
print(f"catctf{{{ret[:20]}}}")
