from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import codecs

class sign_document:
    def __init__(self,file_pdf,file_private_key):
        with open(file_pdf, 'rb') as fp:
            message = fp.read()
        self.key=RSA.import_key(open(file_private_key).read())
        self.h = SHA256.new(message)

    def sign(self):
        signature = pkcs1_15.new(self.key).sign(self.h)
        return signature
    def verify(self,signature):
        try:
            pkcs1_15.new(self.key).verify(self.h, signature)
            print("The signature is valid.")
        except (ValueError, TypeError):
            print ("The signature is not valid.")
if __name__ == '__main__':
    file_private_key='./output/private.pem'
    file_pdf="seni.pdf"
    rsa=sign_document(file_pdf,file_private_key)
    signature=rsa.sign()
    print("Signature:")
    print(signature)
    rsa.verify(signature)
    

