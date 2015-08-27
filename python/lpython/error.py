#!/usr/bin/env python
# -*- coding: utf-8 -*-

#错误处理
#try...except...finally...
import logging

def foo(s):
    return 0/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'

#单元测试

#文档测试

