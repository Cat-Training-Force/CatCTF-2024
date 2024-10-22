import sys
import uuid
from subprocess import check_output


def flag_to_ebcdic(flag: str) -> bytes:
    alphabet = r"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-{} "
    ebcdic = bytes.fromhex(
        "c1 c2 c3 c4 c5 c6 c7 c8 c9 d1 d2 d3 d4 d5 d6 d7 d8 d9 e2 e3 e4 e5 e6 e7 e8 e9 f0 f1 f2 f3 f4 f5 f6 f7 f8 f9 60 c0 d0 40"
    )
    ebcdic_dict = {alphabet[i]: ebcdic[i] for i in range(len(alphabet))}
    ret = []
    for ch in flag.upper():
        ret.append(ebcdic_dict[ch])
    return bytes(ret)


def patch(filename, pos, data):
    with open(filename, "r+b") as f:
        f.seek(pos)
        f.write(data)
    return True


if __name__ == "__main__":
    flag = f"catctf{{{uuid.uuid4()}}}"
    try:
        flag = sys.argv[1]
        assert len(flag) == len("catctf{065fe164-8408-44c3-ac25-145bbda51b7b}")
    except:
        pass
    patch_data = flag_to_ebcdic(flag)
    r = check_output(["cckd2ckd", "dasd/pub001.270", "dasd/pub001.270.ckd"])
    print(r.decode())
    check_output(["rm", "dasd/pub001.270"])
    patch("dasd/pub001.270.ckd", 0x00E5B21D, patch_data)
    r = check_output(["ckd2cckd", "dasd/pub001.270.ckd", "dasd/pub001.270"])
    print(r.decode())
    check_output(["rm", "dasd/pub001.270.ckd"])

'''
2381c2381
< 000094c0: 4040 4040 1801 1300 0000 0040 0090 000c  @@@@.......@....
---
> 000094c0: 4040 4040 1801 1400 0000 0040 0090 000c  @@@@.......@....
940835,940837c940835,940837
< 00e5b220: c3e3 c6c0 d4f4 c9d5 c6d9 c1d4 f3e2 6d7c  ..............m|
< 00e5b230: d9c5 6de2 e4d7 c5d9 6dc3 d6d6 f1d0 4040  ..m.....m.....@@
< 00e5b240: 4040 4040 4040 4040 4040 4040 4040 4040  @@@@@@@@@@@@@@@@
---
> 00e5b220: c3e3 c6c0 c5f1 c6f2 c4c6 c4f8 60f6 f3f4  ............`...
> 00e5b230: f460 f4f1 f4f9 60c1 f3f6 c360 f6f6 c1f6  .`....`....`....
> 00e5b240: f3f0 c6c2 f2c6 c2f7 d040 4040 4040 4040  .........@@@@@@@
'''