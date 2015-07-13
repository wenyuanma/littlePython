# add line number at each of end of each line in a file
import fileinput

for line in fileinput.input(inplace=True, backup='.bakup'):
    line = line.rstrip()
    num = fileinput.lineno()
    print '%-70s # %2i' % (line, num)
