#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
任务
请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
提示：
1. isinstance(x, str) 可以判断变量 x 是否是字符串；
2. 字符串的 upper() 方法可以返回大写的字母。
'''
def toUppers(L):
    sum = []
    for x in L:
        if isinstance(x, str):
            # print x.upper()
            sum.append(x.upper())
    return sum
print toUppers(['Hello', 'world', 101])


def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]
print toUppers(['Hello', 'world', 101])