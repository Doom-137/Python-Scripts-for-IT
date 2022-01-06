import os
import random
import struct
from Crypto.Cipher import AES
import hashlib

def create_key(passkey):
	key = hashlib.sha256(passkey).digest()
	return key

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
#======================================================================================================#
#			Testing Area
#======================================================================================================#
"""
KEEEY = ""
encrypt_file(create_key(KEEEY), "lorem_ipsum.txt", "lorem_eipsum.txt", 32)
"""
#======================================================================================================#
