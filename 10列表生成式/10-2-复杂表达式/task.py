#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
任务
在生成的表格中，对于没有及格的同学，请把分数标记为红色。
提示：红色可以用 <td style="color:red"> 实现。
'''

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score >= 60:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
    else:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)

tds = [ generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
# 注：字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串。


'''
输出结果：
​html代码
​<table border="1">
​<tr><th>Name</th><th>Score</th><tr>
​<tr><td>Lisa</td><td>85</td></tr>
​<tr><td>Adam</td><td>95</td></tr>
​<tr><td>Bart</td><td style="color:red">59</td></tr>
​</table>
'''