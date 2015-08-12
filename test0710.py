import json

class stu:

    def __init__(self, name="lily", age=10):
        self.name = name
        self.age = age

    def speak(self):
        print "my name is %s and my age is %d" % (self.name, self.age)

s = stu("bob", 19)
s.speak()
print s.__dict__

stu_str = '{"name":"lily","age":21}'


def dict2stu(d):
    return stu(d["name"], d['age'])

s1 = json.loads(stu_str, object_hook=dict2stu)
s1.speak()
