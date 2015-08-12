def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log
def now():
    print '2013-12-25'
now()

print now.__name__ 

def log1(func):
    print "call %s():" % func.__name__
    return func


@log1
def now1():
    print '2013-12-26'
now1()

print now1.__name__

# 虽然上述两个函数执行的结果是一样的，但是他们的属性__name__ 就不一样了，
# now的已经变成了wrapper了，但是now1的还是now1


