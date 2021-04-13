#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
=================================================
@Project -> File   ：awesome_python_web -> test
@IDE    ：PyCharm Community Edition
@Author ：Gao Yan
@Date   ：2021/4/6 9:39
@Desc   ：
==================================================
'''


# 协程
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'

# 协程-杨辉三角
def triangles(max):
    list_t = [1]
    n = 0
    print(list_t)
    while n < max:
        n += 1
        list_t2 = []
        for i in range(n+1):
            if i == 0:
                list_t2.append(list_t[0])
            elif i == n:
                list_t2.append(list_t[-1])
            else:
                list_t2.append(list_t[i-1] + list_t[i])
        yield list_t2
        list_t = list_t2
    return 'done'

# send函数
def test():
    n = yield 1
    print("the first n: %d" % n)
    while True:
        n = yield n
        print(n)


if __name__ == '__main__':
    gen = test()
    r = gen.send(None)
    print("first return is %d" % r)
    gen.send(5)
    gen.send(6)
    gen.send(1)