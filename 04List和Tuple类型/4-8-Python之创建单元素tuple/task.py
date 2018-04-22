#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
为什么没有创建出包含一个学生的 tuple
'''

t = ('Adam')
print t
# Adam  字符串

# 正是因为用()定义单元素的tuple有歧义，所以 Python 规定：
# 单元素 tuple 要多加一个逗号“,”，这样就避免了歧义：

T = ('Adam', )
print T