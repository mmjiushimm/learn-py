# -*- coding:utf_8 -*-
# typical closure case
def f(l, x):
    a = 'a in f'
    def inner_f(x):
        sum = 0
        b = 'b in inner_f'
        for i in l:
            sum = sum + i
        print(x, a, b)
        return sum
    return inner_f

l = list(range(10))
in_f = f(l, 'xx')
print(in_f)
sum = in_f('x2')
print(sum)

# how to use variable in closure
# case1 - wrong way
def f_with_variable():
    l = []
    for i in range(5):
        def inner_f():
            return i
        l.append(inner_f)
    return l
    
l_0 = f_with_variable()
for i in l_0:
    print(i())
    
# case2 - correct way
def f_with_variable_1():
    l = []
    def f(i):
        def inner_f():
            return i
        return inner_f
    for i in range(5):
        l.append(f(i))
    return l
    
l_1 = f_with_variable_1()
for i in l_1:
    print(i())