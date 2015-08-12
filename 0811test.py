import functools
from datetime import date
from types import MethodType


def log(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if text:
                for x in text:
                    print x
            print "call begin"
            func(*args, **kw)
            print "call end\n"
            return
        return wrapper
    return decorator


@log("please execute")
def now():
    print "today is % s" % date.today()

now()


@log()
def now1():
    print "today is %i" % (date.today().weekday() + 1)

now1()


class Student():
    pass

s = Student()
s.name = "ivy"


def set_age(self, age):
    self.age = age

s.setage = MethodType(set_age, s, Student)

s.setage(5)

print "%s is %i years old " % (s.name, s.age)
