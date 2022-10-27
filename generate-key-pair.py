from Cryptodome.PublicKey import RSA
import os

key = RSA.generate(2048)
private_key = key.exportKey('PEM')
public_key = key.publickey().exportKey('PEM')

if not os.path.exists('output'):
    os.makedirs('output')

with open('output/private.pem', 'wb') as f:
    f.write(private_key)

with open('output/public.pem', 'wb') as f:
    f.write(public_key)
