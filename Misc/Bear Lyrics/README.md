# Bear Lyrics

## 题面

by *Nemo*

熊老师突然莫名其妙地给你传了一段歌词。你很清楚地知道他不是那种那种天天发莫名其妙的抒情歌词出来的二次元，所以这之中一定隐藏了什么秘密……

## 题解

你应该会想了解一下 Unicode 的基础知识。

仔细观察该文本，会发现很多字符未渲染或者是渲染错误。

理论上来说这时候你去查 Misc / Stego 解题技巧就应该会有那个 [解码器](https://330k.github.io/misc_tools/unicode_steganography.html)

如果你不知道的话，也问题不大；你可以通过十六进制编辑器打开该文件，将奇怪的字符一个个拿出来并且找寻规律 + 解码。

## Flag

`catctf{Me4n_sP@c#_@nD_UNs#En}`