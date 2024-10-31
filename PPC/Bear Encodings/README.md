# Bear Encodings

## 题面

by *Nemo*

熊老师想测试一下你的脚本能力。

## 题解

你可能会想先去了解一下伪随机。

仔细观察代码，发现 `random.seed(seed)`，同时 `seed` 也被打出在文件中。

所以直接调用 seed 来初始化 `random`，然后调用 random 函数就行了。

## Exploit

```python
from base64 import b64decode, b32decode, b16decode
import codecs

def base16(s: str) -> str:
    return b16decode(s.encode()).decode()

def base32(s: str) -> str:
    return b32decode(s.encode()).decode()

def base64(s: str) -> str:
    return b64decode(s.encode()).decode()

def rot13(s: str) -> str:
    return codecs.decode(s, 'rot_13')


ENC_FUNCTIONS = [base16, base32, base64, rot13]

import random

# load from local
# with open('encodings.txt', 'r', encoding='utf-8') as f:
#     seed, result = f.read().splitlines()

# load from network
import requests
r = requests.get('http://127.0.0.1:3270/encodings.txt')
seed, result = r.text.splitlines()

random.seed(int(seed))

steps = []

for i in range(30):
    function = random.choice(ENC_FUNCTIONS)
    steps.append(function)

for step in reversed(steps):
    # result = step(result.lstrip('ftctac{').rstrip('}'))
    result = step(result[7:-1])

print(result)
```

Unintended solution:

其实你自己一个个解码也是可以的，毕竟一定是 `ftctac` 打头。

## 额外说明

其实本来要出交互题的。