# tugas-2-kij-c

Install all dependencies before running any of the program with:

```
pip install -r requirements.txt
```

Using virtual environment is recommended.

## Generate Key Pair

Generate a public and private RSA key pair by running:

```
python3 generate-key-pair.py [-o OUTPUT] [-s SIZE] [-p PASSPHRASE]
```

Options:
```
-h, --help
show help message and exit

-o OUTPUT, --output OUTPUT
Path to directory where the keys will be saved, optional, default is ./output

-s SIZE, --size SIZE
Key size in bits, optional, default is 2048

-p PASSPHRASE, --passphrase PASSPHRASE
Passphrase for the key, optional
```

## Sign a pdf

Sign a pdf file by running:

```
python3 sign-document.py -i INPUT -k KEY [-o OUTPUT] [-a AUTHOR] [-p PASSPHRASE]
```

Options:

```
-h, --help
show help message and exit

-i INPUT, --input INPUT
Path to PDF file to be signed, required

-o OUTPUT, --output OUTPUT
Path to save the signed PDF file, optional, default to output.pdf

-k KEY, --key KEY
Path to private key file, required, generate with generate-key-pair.py if needed
    
-a AUTHOR, --author AUTHOR
Author of the signature, optional, max 60 characters

-p PASSPHRASE, --passphrase PASSPHRASE
Passphrase for the key, optional
```

## Verify a pdf

Verify the signature of a pdf file by running:

```
python3 verify-document.py -i INPUT -k KEY [-p PASSPHRASE]
```

Options:

```
-h, --help
show help message and exit

-i INPUT, --input INPUT
Path to PDF file to be verified, required

-k KEY, --key KEY     
Path to public key file, required, generate with generate-key-pair.py if needed

-p PASSPHRASE, --passphrase PASSPHRASE
Passphrase for the key, optional
```