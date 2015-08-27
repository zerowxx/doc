#!/usr/bin/env python
# -*- coding: utf-8 -*-

#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
def add(x, y, f):
    return f(x) + f(y)
print add(5, -6, abs)

#map/reduce
#python内建map()和reduce()函数。map函数接收两个参数，函数和序列。
def f(x):
    return x*x
print map(f,[1,2,3,4,5])

def a(x,y):
    return x+y
print reduce(a,[1,2,3,4,5])

#filter() 过滤列。接收函数和序列，根据返回值true和false过滤元素
def is_odd(n):
    return n%2 == 1
print filter(is_odd,[1,2,3,4,5,6,7,8])

#sorted 排序
print sorted([3,2,5,1,4])

def reversed_cmp(x,y):
    if(x > y):
        return -1
    if(x < y):
        return 1
    return 0
print sorted([23,1,54,24,44,39],reversed_cmp)

#返回函数
def lazy_sum(*args):
    def sum():
        a = 0
        for n in args:
            a = a + n
        return a
    return sum

f = lazy_sum(1,3,5,7,9)
print f()
#闭包

#匿名函数:关键字lambda表示匿名函数，冒号前面的x表示函数参数
print map(lambda x : x*x,[1,2,3,4])

#装饰器
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log
def now():
    print '现在的时间'
#log()就是装饰器
print now()
#带参数的装饰器
import functools
def logg(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'call %s():' % func.__name__
            return func(*args, **kw)
        return wrapper
    return decorator

#偏函数 设定函数参数默认值
def int2(x, base=2):
    return int(x, base)
print int2('1000000')
#使用functools.partial实现
intto2 = functools.partial(int, base=2)
print intto2('1000000') 


