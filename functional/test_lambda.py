# -*- coding: utf-8 -*-
def is_odd(x):
    return x % 2 == 1

f = filter(is_odd, range(10))
for i in f:
    print(i)

# rewrite by lambda
print('re-implement by lambda')
f1 = filter(lambda x: x % 2 == 1, range(10))
for i in f1:
    print(i)