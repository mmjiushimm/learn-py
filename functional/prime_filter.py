# -*- coding:utf-8 -*-

# generate natural numbers
def natural_number():
    i = 1
    while True:
        yield i
        i = i + 1

# remainder not 0
def is_divisible(i):
    return lambda x : x % i != 0

def prime_picker():
    nn = natural_number()
    yield next(nn)
    start = next(nn)
    yield start
    while True:
        # filter out the numbers whose remainder is 0 divided by the first number in list
        # and make the rest numbers form a new list
        nn = filter(is_divisible(start), nn)
        start = next(nn)
        yield start

pp = prime_picker()
for i in pp:
    if i < 100:
        print(i)
    else:
        break