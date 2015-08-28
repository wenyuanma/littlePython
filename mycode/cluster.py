# -*- coding: utf-8 -*-
def readfile(filename):
	lines = [line for line in file(filename)]
	#拿到了所有的单词
	colnames = lines[0].strip().split('\t')[1:]

def hcluster(rows,distance = pearson):
	distances = {}
	currentclusterid = -1

