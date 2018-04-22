#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
由于 t 包含一个list元素，导致tuple的内容是可变的。能否修改上述代码，让tuple内容不可变？
'''

t = ('a', 'b', ['A', 'B'])
L = t[2]      #将list提取出来，重新赋值
L[0] = ['x']
L[1] = ['y']

print t

T = ('a', 'b', ('A', 'B'))
S = T[2]
# S[0] = ['x']
# S[1] = ['y']
# TypeError: 'tuple' object does not support item assignment
# 由于('A', 'B') 是一个元组，元组的特点是元素指向不可变
print T
