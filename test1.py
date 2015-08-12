from __future__ import division
import functools


int2 = functools.partial(int, base=2)

print int2('010')


print '\'xxx\' is unicode?', isinstance("xxx", unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)

print '10/3', 10 / 3


print dir(int)
