# -*- coding: utf-8 -*-

# v = 10
# a = 11
def f0():
    global v
    v = 20
    s = v + 10
    return s

def f1():
    u = 5
    # nonlocal a
    # v = 16
    # v = 1
    def nest():
        nonlocal u
        # u = 1
        u += 1
        return u
    return nest

if __name__ == '__main__':
    print(f0())
    print(v)
    n = f1()
    print(n())
    print(n())
    # print(u)
    print(v)