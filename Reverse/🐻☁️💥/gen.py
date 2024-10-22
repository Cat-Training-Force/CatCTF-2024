def main():
    import signal
    def a(f):
        def _(sig, frame):
            import ctypes
            import random
            deref = lambda x: ctypes.cast(x, ctypes.POINTER(ctypes.c_size_t))
            f = id(frame)
            addr = deref(deref(f + 24).contents.value + 56).contents.value
            b = ctypes.cast(addr + 8, ctypes.POINTER(ctypes.c_ubyte * 114514)).contents
            random.seed(114514)
            for i, x in enumerate(b':\x1a\xd75L\x93\xe9\xfa4\xc21\x85"r\xe8\xb0&\x03\xbdMe\x8e\xea\xdc\x1eE\xe4\xfe=r\xce\xee\xceo\xc7p(x\xcf\xd5b\xc7\xfc\xe5T\x1ad]\xaa\x93[\xc2x[\x93\x04%\x04\xb3\x11\x1d\xe4aU\x97\xa2\x04\\l5\xb5v\x8a|:\x9f\xae\xae\xf4\xab\xbb\x8ae1Z\xecxl\xab\x1f\xa1\x83\xad\xad\xb7\x05m1\x8el\x03\xdf/2\x95\xe2T}\xdf$\x939\xa8\xc3\xfa"\xb3n\xa0\xc0\xcc\x1cJ\xa9\xc4\xeeg\x88:{\xfcHNw%\xe6\x86\xea\xa1\xd1Xj\xb9\xba\xb4\xb4\xa2\xfd/\x9dL;\x1b\xa0\xa4\'\x8d\x8a\xd2\r\'E\xf6X.\x9an\x89\xbd\x8e%\xa9E\x1cI=\x19\xd1*\xd4\xb7\x1dU\xe1$\x87T\xf7\xa4\xc0g\x06\x99\x85=\xd3\xb6\xf1\xe5\xc5\xc6\xc0'):
                b[i] = x ^ random.getrandbits(8)
        signal.signal(signal.SIGABRT, _)
        f()

    @a
    def _():
        signal.raise_signal(signal.SIGABRT)
        import os
        flag = int.from_bytes(input('flag?').encode())
        if (flag + 2265555651326074039599621123501801118820891307936726037477835692123442711374258931235932818184993536417235) ^ 4440760596783113064314582300781672267288468802132278265680532832087153719526075481537156425248393218070488 == 7792423967677454399135110459256301640520750463723406977025003932981150359873379166489940082229405441463432:
            print('Right!')
        else:
            print('Wrong!')
        os._exit(0)

if __name__ == '__main__':
    import random
    import marshal
    import dis
    main_code = main.__code__
    p = main_code.co_consts[-1]
    dis.dis(p)
    code_p = p.co_code
    print('origin')
    print(list(code_p[56:]))
    modified_code = list(code_p[:56])
    modified_code += [random.getrandbits(7) for _ in range(len(code_p) - 56)]
    print('modified')
    print(modified_code[56:])
    print('inner bytes')
    random.seed(114514)
    print(str(bytes([random.getrandbits(8) ^ x for x in code_p[56:]])))
    new_code_p = p.replace(co_code=bytes(modified_code))
    list_const = list(main_code.co_consts)
    list_const[-1] = new_code_p
    main_code = main_code.replace(co_consts=tuple(list_const))
    with open('out.py', 'w') as out:
        out.write(f'''
import sys
import marshal
if sys.version_info.minor != 12:
    print("This script requires Python 3.12")
    sys.exit(1)
exec(marshal.loads({str(marshal.dumps(main_code))}))
''')

