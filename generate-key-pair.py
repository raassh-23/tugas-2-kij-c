from Cryptodome.PublicKey import RSA
import os
from argparse import ArgumentParser
import sys

def generate_key_pair(output_path="output", key_size=2048, passphrase=None):
    os.makedirs(output_path, exist_ok=True)

    key = RSA.generate(key_size)
    private_key = key.exportKey(format='PEM', passphrase=passphrase)
    public_key = key.publickey().exportKey(format='PEM', passphrase=passphrase)

    with open(os.path.join(output_path, "private.pem"), 'wb') as f:
        f.write(private_key)

    with open(os.path.join(output_path, "public.pem"), 'wb') as f:
        f.write(public_key)

    print("Key pair generated successfully")

if __name__ == "__main__":
    parser = ArgumentParser(
        prog = 'generate-key-pair.py',
        description = 'Generate a public/private RSA key pair'
    )
    parser.add_argument(
        '-o', '--output',
        help = 'Path to directory where the keys will be saved',
        default = 'output'
    )
    parser.add_argument(
        '-s', '--size',
        help = 'Key size in bits',
        default = 2048,
        type = int
    )
    parser.add_argument(
        '-p', '--passphrase',
        help = 'Passphrase for the key',
        default = None
    )

    args = parser.parse_args()
    
    try:
        generate_key_pair(args.output, args.size, args.passphrase)
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)
