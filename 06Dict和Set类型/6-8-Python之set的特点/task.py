#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
'''

months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
s = raw_input('请输入月份：')
x = s.lower()
y = x.title()
if y in months:
    print 'input ok'
else:
    print 'input error'