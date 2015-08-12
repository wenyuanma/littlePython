class P1(object):

    def foo(self):
        print "P1 foo"


class P2():

    def foo(self):
        print "P2 foo"

    def bar(self):
        print "P2 bar"


class C1(P1, P2):
    pass


class C2(P1, P2):

    def bar(self):
        print "C2 bar"


class D1(C1, C2):
    pass
d1 = D1()
d1.foo()  # P1 foo
d1.bar()  # C2 bar


class D2(C2, C1):
    pass
d2 = D2()
d2.foo()  # P1 foo
d2.bar()  # C2 bar
