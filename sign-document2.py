from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

class sign_document:
    def __init__(self,file_private_key,file_public_key):
        key_1 = RSA.importKey(open(file_public_key).read())
        self.cipher_public = PKCS1_v1_5.new(key_1)

        key_2 = RSA.importKey(open(file_private_key).read())
        self.cipher_private = PKCS1_v1_5.new(key_2)
    def encrypt(self,message,length=100):
        res=[]
        for i in range(0,len(message),length):
            res.append(self.cipher_public.encrypt(message[i:i+length]))
        return b''.join(res)
    def decrypt(self,message,length=128):
        res=[]
        for i in range(0,len(message),length):
            res.append(self.cipher_private.decrypt(message[i:i+length],'xyz'))
        return b''.join(res) 
if __name__ == '__main__':
    file_private_key='./output/private.pem'
    file_public_key='./output/public.pem'
    
    # file_pdf="seni.pdf"
    # with open(file_pdf, 'rb') as fp:
    #     message = fp.read()
    message = b'we are different, work hard!'*100

    rsa=sign_document(file_private_key,file_public_key)   
    ciphertext = rsa.encrypt(message,200)
    # print("ciphertext:  "+str(ciphertext))
    message = rsa.decrypt(ciphertext,256)
    print("plaintext:  "+str(message))

    
    

