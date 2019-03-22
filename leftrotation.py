import math
import os
import random
import re
import sys

def leftRotation(a, d):
	rotateResult = []
	ListToString = ''
	for index in a:
		rotateResult = a[d:] + a[:d]
		ListToString = ' '.join(str(e) for e in rotateResult)
		return ListToString	



if __name__ == '__main__':
	nd = input().split()
	n = int(nd[0]) #number of elements
	d = int(nd[1]) #number of rotations
	a = list(map(int, input().rstrip().split()))
	print (leftRotation(a,d))