from custom_lib import DigitalSignature

def signature(file_pdf, file_private_key, output_file):
    pass
        
if __name__ == '__main__':
    file_private_key='./output/private.pem'
    file_public_key='./output/public.pem'
    file_pdf = 'test.pdf'
    
    sign = digital_signature(file_private_key, file_public_key)
    
    signature = sign.signature(file_pdf)
    sign.verify(file_pdf, signature)