from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os

#mode: CBC

def encryptCBC(data,key):
    #pkcs#7 padding before encrypting
    data = pad(data,16)
    #iv 16 bytes random
    iv = os.urandom(16)
    # encrypt
    cipher = AES.new(key, AES.MODE_CBC,iv)
    encryptedData = cipher.encrypt(data)
    return (iv,encryptedData)


def decryptCBC(encryptedData,key,iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = cipher.decrypt(encryptedData)
    data = unpad(data,16)
    return data



#another mode: CTR
def encryptCTR(data,key):
    #pkcs#7 padding before encrypting
    data = pad(data,16)
    #iv 16 bytes random
    iv = os.urandom(16)
    # encrypt
    cipher = AES.new(key, AES.MODE_CTR,iv)
    encryptedData = cipher.encrypt(data)
    return (iv,encryptedData)


def decryptCTR(encryptedData,key,iv):
    cipher = AES.new(key, AES.MODE_CTR, iv)
    data = cipher.decrypt(encryptedData)
    data = unpad(data,16)
    return data


#test with main function:
def main():
    key = os.urandom(16)
    pt = "caubevang02"
    (iv,ct) = encryptCBC(pt.encode(),key)
    print(decryptCBC(ct,key,iv).decode(errors="ignore") == pt)


if __name__ == "__main__":
    main()
