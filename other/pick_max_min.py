# -*- coding: utf-8 -*-
# input numbers, return max and min in all input history
l = []
num_max = num_min = 0
while True:
    num_s = input('input a number: ')
    if num_s == 'end':
        break
    else:
        num = int(num_s)
        if num > num_max:
            num_max = num
        if num < num_min:
            num_min = num
        l.append(num)
        l = sorted(l)
        print('max = %d, min = %d' % (num_max, num_min))
        print('[', end='')
        for i in l:
            if i is l[-1]:
                print(i, end='')
            else:
                print(i, end=', ')
        print(']')