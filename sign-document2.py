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
    # def verify(self,signature):
    #     try:
    #         pkcs1_15.new(self.key).verify(self.h, signature)
    #         print("The signature is valid.")
    #     except (ValueError, TypeError):
    #         print ("The signature is not valid.")
if __name__ == '__main__':
    from Crypto.PublicKey import RSA

    keyPair = RSA.generate(bits=1024)
    print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
    print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")
    # RSA sign the message
    msg = b'A message for signing'
    from hashlib import sha512
    hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
    signature = pow(hash, keyPair.d, keyPair.n)
    print("Signature:", hex(signature))

    # RSA verify signature
    msg = b'A message for signing'
    hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
    hashFromSignature = pow(signature, keyPair.e, keyPair.n)
    print("Signature valid:", hash == hashFromSignature)
    

