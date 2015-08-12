from types import MethodType


class Student(object):

    def __init__(self, n, a):
        self.name = n
        self.age = a

s = Student("mike", 26)


def set_age(self, age):
    self.age = age

print s.age

s.set_age = MethodType(set_age, s, Student)
s.set_age(16)

print s.age


