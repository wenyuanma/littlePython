from functools import partial

# ---------1.partial function--------
int2 = partial(int, base=2)

print int2("100") + int2("110")

max10 = partial(max, 10)

print max10(2, 4, 5)

# ---------2.customize function & @property--------
class shishi(object):
    __slots__ = ('_name', '_age')

    def __len__(self):
        return self._age

    def __init__(self, n="xiaoming"):
        self._name = n

    def __str__(self):
        return "user name : %s user age: %i" % (self._name, self._age)
    __repr__ = __str__

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('the input of age must be an integer')
        if value < 0 or value > 150:
            raise ValueError('age range is 0 from 150')
        self._age = value

    @property
    def name(self):
        return self._name
s = shishi("xiaohong")
print s.name
s.age = 25
# s.name = "xiaonan" #xxxxx
print s.age
print len(s)
print s

#---------------3. iterable & index-----------
class kediedai(object):

    def __init__(self):
        self.number = 0

    def __iter__(self):
        return self

    def next(self):
        self.number = self.number + 1
        if self.number > 5:
            raise StopIteration()
        return self.number

    def __getitem__(self, n):
        self.number = 0
        if isinstance(n, int):
            for x in range(n):
                self.number = self.number + 2
                print self.number
            return self.number
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            L = []
            for x in range(stop):
                self.number = self.number + 2
                if x >= start:
                    L.append(self.number)
            return L

    def __getattr__(self, attr):
        print "the new attribute is %s" % attr

k = kediedai()

for x in k:
    print x
print k[5]
print k[6:9]
k.profession


#-----------------4.getattr and call----------
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == "username":
            return Chain("%s" % self._path)
        return Chain("%s/%s" % (self._path, path))

    def __call__(self, username):
        return Chain("%s/%s" % (self._path, username))

    def __str__(self):
        return self._path

print Chain().status.username("ivy").repository

