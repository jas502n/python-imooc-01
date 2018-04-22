#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
task.py
如果成绩达到60分或以上，视为passed。
假设Bart同学的分数是75，请用if语句判断是否能打印出 passed:
'''

score = int(raw_input('请输入你的成绩：'))
if score >= 60:
    print 'passed\n你的成绩为：',score
else:
    print 'no passed'
