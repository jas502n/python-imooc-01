#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
定义可变参数的目的也是为了简化调用。假设我们要计算任意个数的平均值，就可以定义一个可变参数：
请编写接受可变参数的 average() 函数。
'''

def average(*args):
    s = 0.0
    for i in args:
        s += i
    if len(args)==0:   # 判断args 元组tuple的长度，如果0个元素，代表0分，所以平均分为0.0 或者写成float(0)
        print 0.0
    else:
        print (s / len(args))
average()
average(1, 2)
average(1, 2, 2, 3, 4)