# -*- coding: utf-8 -*-

'test module doc note'

__author__ = 'mz'

import sys

def f():
    l = sys.argv
    if len(l) == 1:
        print(l[0])
    else:
        print(l[-1])
    
if __name__ == '__main__':
    f()
    print('__author__ =', __author__)
    print('__name__ =', __name__)
    print('__doc__ =', __doc__)