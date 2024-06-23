from cryptography.fernet import Fernet

class FernetEncrdecr():
    def encrdecr(self, keyval, data):
        """加密 && 解密"""
        # Write your code here
        key = keyval  # key = Fernet.generate_key()
        f = Fernet(key)
        result = []
        encrdecr = f.encrypt(data)
        result.append(encrdecr)
        result.append(f.decrypt(encrdecr).decode())  # python去除 b'
        # print(result)
        return result

    def encrdecr_key(self, text):
        """加密 && 解密"""
        # 生成密钥cipher_key
        cipher_key = Fernet.generate_key()
        print(cipher_key)
        cipher = Fernet(cipher_key)
        # 进行加密
        encrypted_text = cipher.encrypt(text)
        print(encrypted_text)
        # 进行解密
        decrypted_text = cipher.decrypt(encrypted_text)
        print(decrypted_text)
        return encrypted_text,decrypted_text

    def decrdecr(self, keyval, data):
        """只做解密"""
        # key = Fernet.generate_key()
        key = keyval
        f = Fernet(key)
        result = []
        result.append(f.decrypt(data).decode())  # python 去除 b'
        # print(result)
        return result


if __name__ == '__main__':
    key = b'OTBQDg8NDtSNtGGw35IKevckBrigRBR6a4qpn5WWq6s='
    text = b'pwd123456'
    print(FernetEncrdecr().encrdecr(key,text))
    # print(FernetEncrdecr().encrdecr_key(key))
    # print(FernetEncrdecr().decrdecr(key,text))

