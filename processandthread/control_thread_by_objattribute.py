# -*- coding: utf-8 -*-

import time, threading

class Flag(object):
    go = True

def do(flag):
    for i in range(5):
        if not flag:
            break
        print(i)
        time.sleep(1)

def do1(flag):
    for i in range(5):
        if not flag.go:
            break
        print(i)
        time.sleep(1)


flag = True
t = threading.Thread(target=do, args=(flag,))
t.start()
time.sleep(2)
flag = False
t.join()

'''
flag = Flag()
t1 = threading.Thread(target=do1, args=(flag,))
t1.start()
time.sleep(2)
flag.go = False
t1.join()
'''
