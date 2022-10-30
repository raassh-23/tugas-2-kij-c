from custom_lib.DigitalSignature import DigitalSignature
from argparse import ArgumentParser

def sign(file_pdf, output_file, file_private_key, passphrase):
    ds = DigitalSignature(file_private_key=file_private_key)
    # TODO: implement this function
    pass
        
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

