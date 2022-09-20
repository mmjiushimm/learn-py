# usr/bin/env python3
# -*- coding: utf-8 -*-

# ord and chr
print(ord('a'))
print(ord('人'))
print(chr(100))
print(chr(10000))

# encode and decode
print('123 encode with utf-8 =', '123'.encode('utf-8'))
print('abc encode with ascii =', 'abc'.encode('ascii'))
print('abc encode with uft-8 =', 'abc'.encode('utf-8'))
print('一二三 encode with utf-8 =', '一二三'.encode('utf-8'))
print('abc一二三 encode with utf-8 =', 'abc一二三'.encode('utf-8'))
bytes_encode_1 = '123'.encode('ascii')
print(bytes_encode_1, "decode with utf-8 =", bytes_encode_1.decode())
bytes_encode_2 = '一二三'.encode('utf-8')
print(bytes_encode_2, "decode with utf-8 =", bytes_encode_2.decode('utf-8', errors = 'ignore'))
print('一二三'.encode('ascii'))