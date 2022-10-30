# tugas-2-kij-c

Install all dependencies before running any of the program with:
``` 
pip install -r requirements.txt
```

Using virtual environment is recommended.

## Generate Key Pair
Generate a public and private RSA key pair by running:
```
python3 generate_key_pair.py [-o OUTPUT] [-s SIZE] [-p PASSPHRASE]
```

## Sign a pdf
Sign a pdf file by running:
```
python3 sign-document.py -i INPUT -k KEY [-o OUTPUT] [-p PASSPHRASE]
```

## Verify a pdf
Verify the signature of a pdf file by running:
```
python3 verify-document.py -i INPUT -s SIGNATURE -k KEY [-p PASSPHRASE]
```
