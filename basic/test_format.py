# !/usr/bin/env/python3
# -*- coding:utf-8 -*-

# % token
print('%s' % 'abc')
print('%06d' % 12)
print('%.3f%%' % 1.2345) # %% to print %
print('%x' % 0xff)
print('%s has %d books' % ('彤彤', 4))

# format() built-in function
print('{0}---{1:05d}---{2:.1f}'.format('abc', 123, 1.12345e3))

# f-string
a = 'abc'
b = 1234
c = 1.2345
print(f'f-string test: {a}---{b:06d}---{c:.3f}')

# practise
l = 72
t = 85
p = (85 - 72) / 72 * 100
print(p)
print('promotion is %.1f%%' % p)
print('promotion is {0:.1f}%'.format(p))
print(f'promotion is {p:.1f}%')