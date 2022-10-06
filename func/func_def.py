#-*- codin: utf-8 -*-
def mypow(x):
    return x * x
    
def mypow(x, m = 2): #相同函数名，后定义的会覆盖先定义的
    i = 0
    mul = 1
    for i in range(m):
        mul = mul * x
    return mul

def default_para(x, y, m = 'm', n = 'n'):
    return x, y, m, n
    
def variable_para(*x):
    l = []
    for i in x:
        l.append(i)
    return l