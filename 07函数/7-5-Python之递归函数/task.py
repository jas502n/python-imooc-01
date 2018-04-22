#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
move(n, a, b, c)表示的是有n个盘子在a柱子上，将要移到b柱子上面去
'''

def move(n, a, b, c):
# 如果a柱子上面只有一个盘子，则直接移到c柱子上面去并输出路径，结束递归
    if n == 1:
        print a, '-->', c
        return
    move(n-1, a, c, b)   # 表示的是将n-1的盘子从a柱子上面移到b柱子上面去
    print a, '-->', c   # 输出最下面个盘子移从a移到c的路径
    move(n-1, b, a, c)   # 将b柱子上面的n-1个盘子移动到c柱子上面
move(4, 'A', 'B', 'C')