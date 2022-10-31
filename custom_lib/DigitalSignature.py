from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA

class DigitalSignature:
    def __init__(self, file_private_key=None, file_public_key=None, passphrase=None):
        if file_private_key is not None:
            with open(file_private_key, 'rb') as fp:
                self.private_key = RSA.importKey(fp.read(), passphrase=passphrase)

            if not self.private_key.has_private():
                raise ValueError("The provided private key is not a private key")
        else:
            self.private_key = None

        if file_public_key is not None:
            with open(file_public_key, 'rb') as fp:
                self.public_key = RSA.importKey(fp.read(), passphrase=passphrase)
            
            if self.public_key.has_private():
                raise ValueError("The provided public key is not a public key")
        else:
            self.public_key = None
        
    def _encrypt(self, plaintext):
        if self.private_key is None:
            raise ValueError("No private key available")

        if not 0 <= plaintext < self.private_key.n:
            raise ValueError("Message too large")

        return int(pow(plaintext, self.private_key.d, self.private_key.n))
        
    def _decrypt(self, ciphertext):
        if self.public_key is None:
            raise ValueError("No public key available")

        if not 0 <= ciphertext < self.public_key.n:
            raise ValueError("Message too large")
        return int(pow(ciphertext, self.public_key.e, self.public_key.n))
    
    def signature(self, file_pdf):
        with open(file_pdf, 'rb') as fp:
            message = fp.read()
        hash_value = SHA256.new(message).digest()
        
        plaintext = int.from_bytes(hash_value, 'big')
        result = self._encrypt(plaintext)
        return result.to_bytes(256, 'big')
        
    def verify(self, file_pdf, signature):
        with open(file_pdf, 'rb') as fp:
            message = fp.read()

        hash_value = SHA256.new(message).digest()
        hash_as_int = int.from_bytes(hash_value, 'big')
        
        signature = int.from_bytes(signature, 'big')
        signature_decrypted = self._decrypt(signature)
        
        return signature_decrypted == hash_as_int
        
if __name__ == '__main__':
    file_private_key='./output/private.pem'
    file_private_key2='./output/private2.pem'
    file_public_key='./output/public.pem'
    file_pdf = 'test.pdf'
    
    sign = DigitalSignature(file_private_key, file_public_key)
    sign2 = DigitalSignature(file_private_key2, file_public_key)
    
    signature = sign.signature(file_pdf)
    print(signature.hex())
    print(sign.verify(file_pdf, signature))

    signature2 = sign2.signature(file_pdf)
    print(signature2.hex())
    print(sign2.verify(file_pdf, signature2))

    file_private_key_pass = './output/private_pass.pem'
    file_public_key_pass = './output/public_pass.pem'

    sign_pass = DigitalSignature(file_private_key_pass, file_public_key_pass, "test")

    signature_pass = sign_pass.signature(file_pdf)
    print(signature2.hex())
    print(sign_pass.verify(file_pdf, signature_pass))