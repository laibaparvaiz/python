my_tuple = (0, 1, 2, 3, 4, 5, 6)
foo = tuple(filter(lambda x : x - 0 and x - 1 , my_tuple))
print(foo)

def I():
    s = 'abcdef'
    for c in s[::2]:
        yield c


for x in I():
    print(x, end='')

def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in fun(2):
    print(x, end='');


def o(p):
    def q():
        return '*' * p
    return q


r = o(1)
s = o(2)
print(r() + s())

b = bytearray(3)
print(b)

from datetime import date

date_1 = date(1992, 1, 16)
date_2 = date(1991, 2, 5)

print(date_1 - date_2)

import calendar
print(calendar.weekheader(2))

import math 
print(dir(math))

print(__name__)

x = "\\\\"
print(len(x))

print(chr(ord('p') + 2))

print(float("1.3"))

class A:
    def __init__(self, v=2):
        self.v = v

    def set(self, v=1):
        self.v += v
        return self.v


a = A()
b = a
b.set()
print(a.v)

class A:
    A = 1
    def __init__(self):
        self.a = 0


print(hasattr(A, 'a'))

class A:
    pass


class B(A):
    pass


class C(B):
    pass


print(issubclass(A, C))

class A:
    def a(self):
        print('a')


class B:
    def a(self):
        print('b')


class C(B, A):
    def c(self):
        self.a()


o = C()
o.c()

def my_fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in my_fun(2):
    print(x, end='')

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x, end='')

def o(p):
    def q():
        return '*' * p
    return q


r = o(1)
s = o(2)
print(r() + s())

from datetime import datetime

datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

print(datetime_1 - datetime_2)

from datetime import timedelta

delta = timedelta(weeks = 1, days = 7, hours = 11)
print(delta * 2)

import calendar

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.weekheader(3))








