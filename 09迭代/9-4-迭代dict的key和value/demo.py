#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
demo.py
'''

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}

print d.items()

# [('Lisa', 85), ('Adam', 95), ('Bart', 59)]

for key, value in d.items():
    print key, ':', value

# 和 values() 有一个 itervalues() 类似

# items() 也有一个对应的 iteritems()

# iteritems() 不把dict转换成list，而是在迭代过程中不断给出 tuple，所以， iteritems() itervalues() 不占用额外的内存。

