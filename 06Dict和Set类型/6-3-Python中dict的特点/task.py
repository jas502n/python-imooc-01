#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
请设计一个dict，可以根据分数来查找名字，已知成绩如下：
Adam: 95,
Lisa: 85,
Bart: 59.
'''

dict = {
    95 : 'Adam',
    85 : 'Lisa',
    59 : 'Bart'
}
s = int(raw_input('请输入你要查的分数：'))
print dict.get(s)