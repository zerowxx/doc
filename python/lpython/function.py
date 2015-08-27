#!/usr/bin/env python
# -*- coding: utf-8 -*-

#函数相关

#位置参数与默认参数
def power(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
#x,n为位置参数
print power(2,4)

def power1(x, n=2):
    s = 1
    while n > 0:
         n = n - 1
         s = s * x
    return s
#n为默认参数，当你未附值时，为默认值；必选参数在前，默认参数在最后；默认参数必须为不变对象
print power1(2)

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
#参数前加*表示可变参数
nums = [1,2,3]
print calc(*nums)
#函数调用亦可用*将list或tuple转为可变参数

#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:',name,'age:',age,'other',kw)

print person('Michael', 39)
print person('Bob', 23, city='HangZhou', job='Engineer')

#命名关键字参数，限制关键字参数，*分隔符后面的参数为命名关键字参数，可设默认值，否则必须传
def person1(name, age, *, city, job):
    print(name, age, city, job)

#参数组合
#除了可变参数无法和命名关键字参数混合。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。

#小结
#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#要注意定义可变参数和关键字参数的语法：
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
#以及调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#定义命名的关键字参数不要忘了写分隔符*，否则定义的将是位置参数。


#递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n - 1)
#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
#解决递归调用栈溢出的方法是通过尾递归优化,尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def fact_iter(num, product):
    if num == 1:
         return product
     return fact_iter(num - 1, num * product)
#大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。




