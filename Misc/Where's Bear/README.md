# [OSINT] Where's Bear

## 题面

你成功找到了前一题中熊老师约饭的地方（假设），并去到了那个地方。结果发现熊老师不见了！

此时，熊老师用秘密信道和你建立了联系，并说他被绑架了！

熊老师告诉你之前他刚用另外一种方式告诉了别人位置，但熊老师的电脑被没收了。

好消息是，熊老师用随身的工具设法从屋子里的网络设备上拿到了当时的流量并传给了你。

熊老师的命运现在就掌握在你的手上……

请找到熊老师的位置，并用如下脚本编码熊老师的位置，精确到哪栋塔。

注意：输入应该是以全名 + [空格] + Tower + [空格] + 塔编号形式：

```
1. 该地区全名，若有空格，空格区分开来的几个单词首字母均大写。
2. Tower
3. 编号（如果你看到了 ABC... 和 123... ，用任意一个均可。）
```

如：`Fudan University Guang Hua Towers Tower 2`。

```python
from hashlib import sha256

def bear_hash(s: str):
    h = sha256(b"bear_bear{" + s.encode() + b"}")
    return h.hexdigest()

def enc(source: str) -> str:
    ret = source
    for _ in range(60):
        ret = bear_hash(ret)
    return f"catctf{{{ret}}}"

print(enc(input("Where: ")))
```

提示 1：针对流量分析的初学者：你可能会先想学习一下什么是 TCP/IP。

提示 2：针对流量分析的初学者：如果你先找到的是 payload，你可能会想学习一下怎么使用你所使用的网络数据包分析器（如 Wireshark）的过滤器功能。

## 解释

首先看到了一个 pcapng 文件，用 Wireshark 打开，发现是一个流量。

遍历 TCP 请求（你可以先把包导出，用别的工具进行分析）找到那个连接，然后跟踪字节流找到这个对话。

用对话中指定的端口筛选那个连接并导出对象，发现是一个不知道是啥的东西，但是对话中提到了 uuencode，所以直接用 uudecode 解码就行了。

解码出来得到一张图片，仔细往远处看能看到 Queen Victoria Market，所以这个地方是 Melbourne。

在谷歌地图（或者苹果，或者百度也行）上找到 QV Market，然后找到附近的塔，一个个试就能找到答案了。

理论上按照角度能直接确定唯一的塔，但是实际上可能会有一些误差，所以可能需要多试几次。

`West Side Place Tower 2` 或者 `West Side Place Tower B`。

## Flag

`catctf{c843850721a88596a5c3a5bcec18779402ae9ac6c0e37eddc183f26c90b60962}`

或者

`catctf{6b2701c35da4d510ffebfa298db07d50f78111dbd1be47352fe452bb31e62a2a}`