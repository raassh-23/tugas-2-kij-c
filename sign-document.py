from custom_lib.DigitalSignature import DigitalSignature
from custom_lib.SignatureUtil import add_signature
from argparse import ArgumentParser
import sys

def sign(file_pdf, output_file, file_private_key, author, passphrase):
    ds = DigitalSignature(file_private_key=file_private_key, passphrase=passphrase)
    signature = ds.signature(file_pdf)

    add_signature(file_pdf, output_file, signature, author)

    print("File signed successfully")
        
if __name__ == '__main__':
    parser = ArgumentParser(
        prog = 'sign-document.py',
        description = 'Sign a pdf document'
    )
    parser.add_argument(
        '-i', '--input',
        help = 'Path to PDF file to be signed',
        required = True
    )
    parser.add_argument(
        '-o', '--output',
        help = 'Path to save the signed PDF file',
        default='output.pdf'
    )
    parser.add_argument(
        '-k', '--key',
        help = 'Path to private key file, generate with generate-key-pair.py if needed',
        required = True
    )
    parser.add_argument(
        '-a', '--author',
        help = 'Author of the signature, max 60 characters',
        default = None
    )    
    parser.add_argument(
        '-p', '--passphrase',
        help = 'Passphrase for the key',
        default = None
    )

    args = parser.parse_args()

    try:
        sign(args.input, args.output, args.key, args.author, args.passphrase)
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)

