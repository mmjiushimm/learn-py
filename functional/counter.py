# -*- coding:utf-8 -*-
def counter():
    i = 0
    def inner_f():
        nonlocal i # exterior variable can be modified by nonlocal variable in inner func
        i = i + 1
        return i
    return inner_f
    
timer = counter()
for i in range(5):
    print(timer())
timer1 = counter()
for i in range(6):
    print(timer1())