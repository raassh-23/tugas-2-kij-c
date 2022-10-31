from custom_lib.DigitalSignature import DigitalSignature
from argparse import ArgumentParser
from datetime import datetime
from custom_lib.SignatureUtil import get_signature, get_content, add_signature
from PyPDF2 import PdfReader, PdfWriter

def verify(file_pdf, file_public_key, passphrase):
    ds = DigitalSignature(file_public_key=file_public_key)
    
    signature_info = get_signature(file_pdf)
    signature = bytes.fromhex(signature_info['Signature'])
    content = get_content(file_pdf)

    if ds.verify(content, signature):
        print("File verified successfully.")
        print("Author: " + signature_info['Author']) if signature_info['Author'] != "" else None
        print("Date: " + datetime.strptime(signature_info['Date'], "%Y%m%d%H%M%S").strftime("%d/%m/%Y %H:%M:%S"))
    else:
        print("File verification failed.")

    pass
        
if __name__ == '__main__':
    parser = ArgumentParser(
        prog = 'verify-document.py',
        description = 'Verify a pdf document'
    )
    parser.add_argument(
        '-i', '--input',
        help = 'Input file',
        required = True
    )
    parser.add_argument(
        '-k', '--key',
        help = 'Public key file',
        required = True
    )
    parser.add_argument(
        '-p', '--passphrase',
        help = 'Passphrase',
        default = None
    )

    args = parser.parse_args()

    try:
        verify(args.input, args.key, args.passphrase)
    except Exception as e:
        print(f'Error: {e}')
