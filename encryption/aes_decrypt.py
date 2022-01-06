import os
import random
import struct
from Crypto.Cipher import AES
import hashlib

def create_key(passkey):
	key = hashlib.sha256(passkey).digest()
	return key

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
#======================================================================================================#
#			Testing Area
#======================================================================================================#
"""
KEEEY = ""
decrypt_file(create_key(KEEEY), "lorem_eipsum.txt", "lorem_dipsum.txt", 32)
"""
#======================================================================================================#
