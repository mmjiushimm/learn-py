# -*- coding: utf-8 -*-
import functools
def d(f):
    def wrapper(*args, **kw):
        print('start')
        print(f(*args, **kw))
        print('end')
        #return re
    return wrapper

def d_with_parameter(*args):
    def d(f):
        @functools.wraps(f)
        def wrapper(*args1, **kw):
            print('start')
            print(args)
            print(f(*args1))
            print('end')
        return wrapper
    return d

#@d
@d_with_parameter(111)
def f(args):
    return args
    

print(f(12))
print(f.__name__)