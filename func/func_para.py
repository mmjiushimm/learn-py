# -*- coding: utf-8 -*-
from func_def import mypow
from func_def import default_para
from func_def import variable_para

print('mypow(4) =', mypow(4))
print('mypow(0, 2) =', mypow(0, 0))

print(default_para(2, 3))
print(default_para(2, 3, 'mmm'))
print(default_para(2, 3, 'nnn'))
print(default_para(2, 3, m = 'fff'))
print(default_para(2, 3, n = 'ddd'))

print(variable_para(1, 2, 3))
