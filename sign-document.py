from custom_lib.DigitalSignature import DigitalSignature
from custom_lib.SignatureUtil import add_signature
from argparse import ArgumentParser
from PyPDF2 import PdfReader, PdfWriter

def sign(file_pdf, output_file, file_private_key, passphrase):
    ds = DigitalSignature(file_private_key=file_private_key)
    signature = ds.signature(file_pdf)

    add_signature(file_pdf, output_file, signature)

    print("File signed successfully")
        
if __name__ == '__main__':
    parser = ArgumentParser(
        prog = 'sign-document.py',
        description = 'Sign a pdf document'
    )
    parser.add_argument(
        '-i', '--input',
        help = 'Input file',
        required = True
    )
    parser.add_argument(
        '-o', '--output',
        help = 'Output file',
        default='output.pdf'
    )
    parser.add_argument(
        '-k', '--key',
        help = 'Private key file',
        required = True
    )
    parser.add_argument(
        '-p', '--passphrase',
        help = 'Passphrase',
        default = None
    )

    args = parser.parse_args()

    try:
        sign(args.input, args.output, args.key, args.passphrase)
    except Exception as e:
        print(f'Error: {e}')

