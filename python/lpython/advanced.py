#!/usr/bin/env python
# -*- coding: utf-8 -*-

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L
print '切片第一到第三个:',L[0:3]

l = list(range(100))
print '前10',l[:10]
print '后10', l[-10:]
print '20-30', l[20:30]
print '前10每3取',l[:10:3]
print '每30取', l[::30]
print '[ABCDEFG]前3','ABCDEFG'[:3]

#迭代 for...in
d = {'a':1,"b":2}
for key in d:
    print key,':',d.get(key)
for v in d.values():
    print v

from collections import Iterable
print '/"abc/"是否可迭代', isinstance('abc',Iterable)

#列表生成式
print '列表表达式生成前10的平方', [x*x for x in range(1,11)]
print '列表表达式生成前10偶数的平方', [x*x for x in range(1,11) if x%2 ==0]
print '两层循环生成全拍列', [m + n for m in 'ABC' for n in 'XYZ']

#生成器 generator
g = (x*x for x in range(10))
for n in g:
    print n
#若函数定义中包含yield关键字,就是一个生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b
        a,b = b, a + b
        n = n + 1
    return 'done'

#迭代器
#可迭代对象：1.集合数据类型:list,tuple,dict,set,str; 2.generator
#生成器都是Iterator对象,但list,dict,str可迭代，但不是Iterator
