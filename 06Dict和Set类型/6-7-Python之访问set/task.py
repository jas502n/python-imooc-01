#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
由于上述set不能识别小写的名字，请改进set，使得 'adam' 和 'bart'都能返回True。
'''

s = set(['Adam', 'Lisa', 'Bart', 'Paul'])


r = raw_input('请输入一个名字：')
# 先转换成小写，然后转换成大写
x = r.lower()
y = x.title()
print '转换成首字母大写为: %s' % y
if y in s:
    print 'True'
else:
    print 'False'