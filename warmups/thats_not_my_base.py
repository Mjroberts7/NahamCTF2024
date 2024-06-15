#!/bin/env python3

import base64
import re
# to decode from base 85)

def sanitize_base85_string(b85_string):
	valid_chars = re.compile(r'[!-u]')
	sanitized_string = ''.join(valid_chars.findall(b85_string))
	return sanitized_string


encoded_string = r"F#S<YRXdP0Fd=,%J4c$Ph7XV(gF/*]%C4B<qlH+%3xGHo)\""
sanitized_string = sanitize_base85_string(encoded_string)

print(f'Sanitized String: {sanitized_string}')
try:
	decoded_bytes = base64.b85decode(sanitized_string)
	decoded_string = decoded_bytes.decode('utf-8')
	print('Decoded Bytes:', decoded_bytes)
except ValueError as e:
	print(f'error decoding Base85 string: {e}')

