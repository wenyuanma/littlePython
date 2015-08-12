import numpy as np

arr = np.random.randn(7)
arr1 = arr* 5
arr2 = np.modf(arr1)

arr4 = [1,2,3,4]
arr5 = [5,6,7,8]
x,y = np.meshgrid(arr4,arr5)
mul = np.sqrt(x**2+y**2)

arr6 = np.array([[1,2,3,4],[5,6,7,8]])
arrsum1 = arr6.sum(0)
arrsum2 = arr6.sum(1)



print "*********1"
print arr
print "*********2"
print arr1
print "*********3"
print arr2


print "*********x"
print x
print "*********y"
print y
print "*********mul"
print mul
print "*********sum"
print arrsum1
print arrsum2


print "\n"
print "\n"

print np.ones(3)

print np.dot(np.array([[1,2,3],[4,5,6]]),np.ones(3))

help( np.dot)

