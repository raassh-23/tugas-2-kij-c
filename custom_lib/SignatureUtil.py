# SIGNATURE FORMAT
# <<signature
# /Signature (signature)
# /Date (D:20201001120000+00'00')
# /Author (Author)
# signature>>
import datetime
from io import BytesIO

def get_signature(file_pdf):
    fp = open(file_pdf, 'rb')
    lines = fp.readlines()
    file_signature = lines[-1]

    if file_signature != b"signature>>":
        raise Exception("No signature found")

    signature = {}
    for line in lines[-5:]:
        line = line.decode().strip()
        if line.startswith("/"):
            key, value = line.split(" ")
            signature[key[1:]] = value[1:-1]

    fp.close()

    return signature

def get_content(file_pdf):
    input = open(file_pdf, 'rb')

    with BytesIO() as fp:
        fp.write(input.read().split(b"\n<<signature")[0])
        file_content = fp.getvalue()
    
    input.close()
    return file_content

def add_signature(file_pdf, output, signature, author = None):
    with open(file_pdf, 'rb') as fp:
        file_signature = fp.readlines()[-1]
        if file_signature == b"signature>>":
            raise Exception("File already signed")

    f = open(output, "wb+") if output != file_pdf else open(file_pdf, "ab+")
    if output != file_pdf:
        original = open(file_pdf, 'rb')
        f.write(original.read())
        original.close()

    signature = signature.hex()

    f.write(b"\n<<signature")
    f.write(b"\n/Signature (" + signature.encode() + b")")
    f.write(b"\n/Date (" + datetime.datetime.now().strftime("%Y%m%d%H%M%S%z").encode() + b")")
    # f.write(b"\n/Author (" + (author.encode() if author else b"") + b")")
    f.write(b"\nsignature>>")

    f.close()