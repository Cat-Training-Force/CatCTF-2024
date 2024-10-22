from Crypto.PublicKey import RSA
import base64
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import random
from sympy import isprime, mod_inverse

public_key = (65537, 1877516540134765174037595119740214895393637138658476921094107745270653261589372660308043586364634881051739672501738623094431491148929711239284730519792389)
private_key = (381164190708959071067796863880610329786415950224316575906085166407159950035016092363436786499585357961357053982992345387339817622419899103634462778769313,
               1877516540134765174037595119740214895393637138658476921094107745270653261589372660308043586364634881051739672501738623094431491148929711239284730519792389)


# 加密函数
def rsa_encrypt(plaintext: bytes) -> bytes:
    e, n = public_key
    return int_to_bytes(pow(bytes_to_int(plaintext), e, n))


# 解密函数
def rsa_decrypt(ciphertext: bytes) -> bytes:
    d, n = private_key
    return int_to_bytes(pow(bytes_to_int(ciphertext), d, n))


# 字节流转换为整数
def bytes_to_int(message):
    return int.from_bytes(message, byteorder='big')


# 整数转换为字节流
def int_to_bytes(message_int):
    byte_length = (message_int.bit_length() + 7) // 8  # 计算字节长度
    return message_int.to_bytes(byte_length, byteorder='big')


# 使用AES加密数据
def aes_encrypt(plaintext, aes_key) -> bytes:
    # 生成随机的初始向量IV
    iv = get_random_bytes(16)
    cipher_aes = AES.new(aes_key, AES.MODE_CFB, iv)
    ciphertext = cipher_aes.encrypt(plaintext)
    return iv + ciphertext  # 把IV附加到密文的开头


# 使用AES解密数据
def aes_decrypt(ciphertext, aes_key) -> bytes:
    iv = ciphertext[:16]  # 提取IV
    cipher_aes = AES.new(aes_key, AES.MODE_CFB, iv)
    plaintext = cipher_aes.decrypt(ciphertext[16:])
    return plaintext


def encrypt(plaintext: bytes) -> bytes:
    aes_key = get_random_bytes(32)
    enc_aes_key = rsa_encrypt(aes_key)
    ciphertext = aes_encrypt(plaintext, aes_key)
    return (base64.b64encode(ciphertext) + b'.' + base64.b64encode(enc_aes_key))


def decrypt(ciphertext: bytes) -> bytes:
    sp_point = ciphertext.index(b'.')
    enc_aes_key = base64.b64decode(ciphertext[sp_point + 1:])
    ciphertext = base64.b64decode(ciphertext[:sp_point])
    decrypted_aes_key = rsa_decrypt(enc_aes_key)
    decrypted_message = aes_decrypt(ciphertext, decrypted_aes_key)
    return decrypted_message


    # 示例：用RSA加密AES密钥，再用AES加密文本
if __name__ == "__main__":
    message = b'Hello World' * 30
    m = encrypt(message)
    print(m)
    print(decrypt(m))
