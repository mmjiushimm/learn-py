# !/usr/bin/env/python3
# -*- coding:utf-8 -*-

l = ['abc', 123, [1, 'a'], 1.10]
print('list l = ', l)
print('length of l = ', len(l))
print('length of l[2] = ', len(l[2]))
print('l[2] = ', l[2])
print('l[2][1] = ', l[2][1])
print('l[-1] = ', l[-1])
print('id of l = ', id(l))
l.append(True)
print('l append element = ', l)
print('id of new l = ', id(l))
l.insert(1, 0xff)
print('l insert element = ', l)
print('id of new l = ', id(l))