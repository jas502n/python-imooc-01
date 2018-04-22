#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
任务
字符串有个方法 upper() 可以把字符变成大写字母：

'abc'.upper()
'ABC'
但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。

提示：利用切片操作简化字符串操作。
'''



# 自定义前几个字符大写

def StrUpper(s,n=1):
    return s[:n].upper()+s[n:]

print StrUpper('hello',2)
print StrUpper('sunday')
print StrUpper('september')