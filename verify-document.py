from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import codecs

class verify_document:
    def __init__(self, file_pdf, file_public_key):
        with open(file_pdf, 'rb') as fp:
            message = fp.read()
            
        self.publicKey = RSA.import_key(open(file_public_key).read())
        self.h = SHA256.new(message)
    
    def verify(self, signature):
        try:
            pkcs1_15.new(self.publicKey).verify(self.h, signature)
            print("The signature is valid.")
        except (ValueError, TypeError):
            print ("The signature is not valid.")