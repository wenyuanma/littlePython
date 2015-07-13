t1 = {"no", "12"}

d1 = dict(t1)

print d1

t2 = [("name", "lily"), ("age", 12), ("grade", 4)]

d2 = dict(t2)

print d2

integer = 1
print isinstance(integer, (float, int, str))

print range(1, 10)


class Fibos (object):

    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        print "next element is:\n"
        return self

fibs = Fibos()
print fibs.next()
print fibs.next()
print fibs.next()
print fibs.next()
print fibs.next()