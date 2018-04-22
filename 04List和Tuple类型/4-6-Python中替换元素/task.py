#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
Bart同学意外取得第一，而Adam同学考了倒数第一
通过对list的索引赋值，生成新的排名
'''

L = ['Adam', 'Lisa', 'Bart']
L[0] = 'Bart'
# Bart同学意外取得第一
L[-1] = 'Adam'
# Adam同学考了倒数第一
print '新的排名:\n', L