from datetime import date
import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s ():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log
def now():
    print "now is %s " % date.today()

now()


def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print "%s call function %s ():" % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log1("please execute ")
def now1():
    print "today is %s" % date.today()

now1()


def log2(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print "call begin "
            if text:
                print text
            func(*args, **kw)
            print "call end \n"
            return
        return wrapper
    return decorator


@log2()
def now3():
    print "3 today is %s" % date.today()

now3()


@log2("please execute")
def now4():
    print "4 today is %s" % date.today()

now4()
