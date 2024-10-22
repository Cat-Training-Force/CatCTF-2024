import re
from hashlib import sha256


def bear_hash(s: str):
    h = sha256(b"bear_bear{" + s.encode() + b"}")
    return h.hexdigest()


station = "Kunsthaus"
assert re.fullmatch("[A-Z][a-z]+", station)
ret = station
n = 0
for i in range(3213348144):
    ret = bear_hash(ret)
print(f"catctf{{{ret}}}")
