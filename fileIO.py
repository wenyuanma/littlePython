with open("/Users/mwy/Documents/learnpython/test1.py", 'r') as f:
    i = 0
    for line in f.readlines():
        i += 1
        print "~~~~~~~%s line:" % i
        print(line)


with open("/Users/mwy/Documents/learnpython/test2.py", 'a') as f2:
	f2.write("my first write file with python")
	f2.writelines("the second line")
	f2.writelines("the third lines")
