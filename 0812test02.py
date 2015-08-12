# -*- coding: utf-8 -*-

# type() 可以动态地创建类型


def func(self, name='world'):
    print 'hello, %s' % name
Hello = type('Hello', (object,), dict(hello=func))

h = Hello()

h.hello("ivy")


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero !'
    return 10 / n
print foo(0)
