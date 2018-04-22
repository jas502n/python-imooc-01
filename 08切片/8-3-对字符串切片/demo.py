#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
字符串 'xxx'和 Unicode字符串 u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
'''

print 'ABCDEFG'[:3]


print 'ABCDEFG'[-3:]


print 'ABCDEFG'[::2]

print '\n默认首字母大写\n'

def firstCharUpper(s):
    return s[:1].upper()+s[1:]

print firstCharUpper('hello')
print firstCharUpper('sunday')
print firstCharUpper('september')