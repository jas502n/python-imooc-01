#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Python中，迭代永远是取出元素本身，而非元素的索引。
对于有序集合，元素确实是有索引的。有的时候，我们确实想在 for 循环中拿到索引，怎么办？
方法是使用 enumerate() 函数：
'''

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index, '-', name

# 使用 enumerate() 函数，我们可以在for循环中同时绑定索引index和元素name。但是，这不是 enumerate() 的特殊语法。实际上，enumerate() 函数把：
# ['Adam', 'Lisa', 'Bart', 'Paul'] 变成了类似： [(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]




