#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
完全可以通过一个复杂的列表生成式把它变成一个 HTML 表格：
'''

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }

tds = ['<tr> <td> %s </td> <td> %s </td> </tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

# 注：字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串。

