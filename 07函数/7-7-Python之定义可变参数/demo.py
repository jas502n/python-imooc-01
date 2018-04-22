#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
 可变参数的名字前面有个 * 号，我们可以传入0个、1个或多个参数给可变参数：
'''

def fn(*args):
    print args

fn()
fn('a')
fn('a', 'b')
fn('a', 'b', 'c')

# 可变参数也不是很神秘，Python解释器会把传入的一组参数组装成一个tuple传递给可变参数，
# 因此，在函数内部，直接把变量 args 看成一个 tuple 就好了。




