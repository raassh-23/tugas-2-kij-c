from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class sign_document:
    def __init__(self,file_private_key,file_public_key):
        key = RSA.importKey(open(file_public_key).read())
        self.cipher_public = PKCS1_OAEP.new(key)
        key = RSA.importKey(open(file_private_key).read())
        self.cipher_private = PKCS1_OAEP.new(key)
    def encrypt(self,message):
        ciphertext = self.cipher_public.encrypt(message)
        return ciphertext 
    def decrypt(self,message):
        plaintext = self.cipher_private.decrypt(message)
        return plaintext 
if __name__ == '__main__':
    file_private_key='./output/private.pem'
    file_public_key='./output/public.pem'
    # file_pdf="seni.pdf"
    # with open(file_pdf, 'rb') as fp:
    #     message = fp.read()
    message = b'You can attack now!'
    rsa=sign_document(file_private_key,file_public_key)   
    ciphertext = rsa.encrypt(message)
    message = rsa.decrypt(ciphertext)
    print(message)

    
    

