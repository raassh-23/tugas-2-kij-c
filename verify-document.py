from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

class digital_signature:
    def __init__(self, file_private_key, file_public_key):
        self.publicKey = RSA.importKey(open(file_public_key).read())
        self.privateKey = RSA.importKey(open(file_private_key).read())
        
    def encrypt(self, plaintext):
        if not 0 <= plaintext < self.privateKey.n:
            print("Message is too large")
        return int(pow(plaintext, self.privateKey.d, self.privateKey.n))
        
    def decrypt(self, ciphertext):
        if not 0 <= ciphertext < self.publicKey.n:
            print("Message is too large")
        return int(pow(ciphertext, self.publicKey.e, self.publicKey.n))
    
    def signature(self, file_pdf):
        with open(file_pdf, 'rb') as fp:
            message = fp.read()
        hash = SHA256.new(message).digest()
        
        plaintext = int.from_bytes(hash, 'big')
        result = self.encrypt(plaintext)
        return result.to_bytes(256, 'big')
        
    def verify(self, file_pdf, signature):
        with open(file_pdf, 'rb') as fp:
            message = fp.read()
        hash = SHA256.new(message).digest()
        
        signature = int.from_bytes(signature, 'big')
        result = self.decrypt(signature)
        result = result.to_bytes(32, 'big')
        
        if result == hash:
            print("The signature and file is valid!")
        else:
            print("The signature and file is not valid!")
        
if __name__ == '__main__':
    file_private_key='./output/private.pem'
    file_public_key='./output/public.pem'
    file_pdf = 'test.pdf'
    
    sign = digital_signature(file_private_key, file_public_key)
    
    signature = sign.signature(file_pdf)
    sign.verify(file_pdf, signature)