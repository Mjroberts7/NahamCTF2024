#!/bin/env python3

import lzma
import base64

#comp_file = 'theflag.xz?token=eyJ1c2VyX2lkIjozMzA1LCJ0ZWFtX2lkIjoxODExLCJmaWxlX2lkIjo3Nn0.Zk_7Vg.QpyjsS1S4XCH43-qJGKK2wdfiYk'
decomp_file = 'theflag.xz'

'''with lzma.open(comp_file, 'rb') as cfile:
	with open(decomp_file, 'wb') as dfile:
		dfile.write(cfile.read())
'''

#print(f'Decompressed file: {decomp_file}')
base32_enc_file = decomp_file
base32_decoded_file = 'base3200'


with open(base32_enc_file, 'rb') as bfile:
	bencode = bfile.read()

decoded_data = base64.b32decode(bencode)

with open(base32_decoded_file, 'wb') as d:
	d.write(decoded_data)

print(f' base 3200 decoded to: {base32_decoded_file}')
