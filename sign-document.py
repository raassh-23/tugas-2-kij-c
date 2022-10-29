from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

class sign_document:
    def __init__(self,message,file_location):
        self.key=RSA.import_key(open(file_location).read())
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
    message = b'To be signed'
    file_location='./output/private.pem'
    
    rsa=sign_document(message,file_location)
    signature=rsa.sign()
    print(signature)
    
    rsa.verify(signature)
    

