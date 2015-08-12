import numpy as np

names = np.array(['lily', 'bob', 'alice', 'lily'])

data = np.array([[1, 2, 3, 4], [12, 13, 14, 15], [23, 24, 25, 26], [34, 35, 36, 37]])

print names == 'lily'

print data[names != 'lily']

print data[names == 'lily']

print"--------"

print data.T

data[data < 4] = 0

print data

print "*************"

print np.random.randn(7)