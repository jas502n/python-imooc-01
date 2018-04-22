#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
如果成绩达到60分或以上，视为passed，否则视为failed。
假设Bart同学的分数是55，请用if语句打印出 passed 或者 failed:
'''

score = int(raw_input('请输入你的成绩：'))
if score >= 60 :
    print 'passed'
else:
    print 'failed'

print '你的分数为%s分' % score