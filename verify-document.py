from custom_lib.DigitalSignature import DigitalSignature
from argparse import ArgumentParser

def verify(file_pdf, file_signature, file_public_key, passphrase):
    ds = DigitalSignature(file_public_key=file_public_key)
    # TODO: implement this function
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
        '-s', '--signature',
        help = 'Signature file',
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
        verify(args.input, args.signature, args.key, args.passphrase)
    except Exception as e:
        print(f'Error: {e}')
