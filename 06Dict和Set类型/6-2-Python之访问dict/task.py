#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
请打印出：
Adam: 95
Lisa: 85
Bart: 59
'''
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for x in list(d):
    print "%s: %d" % (x,d.get(x))

# %d 整型
# %s 字符串
# %f 浮点型


