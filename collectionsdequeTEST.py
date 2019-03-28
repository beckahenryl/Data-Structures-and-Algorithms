'''
input:
- integer, the number of operations
- space separated names of methods and their values- array

output:
- print out the space separated elements of deque d

task:
- perform methods on an empty deque- append,
pop, popleft, appendleft

	#split the values within original list to separate
	#the string method from the integer value

	for index in methodAndValue:
		performOperation.append(index.split())

'''
from collections import deque
import re

numberOperations = int(input())

methodAndValue = []


#get method and value, store into list
for i in range (0, numberOperations):
	i = input()
	methodAndValue.append(i)


def collectionsDeque (numberOperations, methodAndValue):

	performOperation = []

	d = deque()

	#split the values within original list to separate
	#the string method from the integer value

	for index in methodAndValue:
		performOperation.append(index.split())

	for i in performOperation:
		if i[0] == 'append':
			d.append(i[1])
		if i[0] == 'pop':
			d.pop()
		if i[0] == 'popleft':
			d.popleft()
		if i[0] == 'appendleft':
			d.appendleft(i[1])
	
	toList = list(d)
	changeIndexToInt = [int(i) for i in toList]
	stringFromList = ' '.join(str(e) for e in changeIndexToInt)

	return stringFromList					

print (collectionsDeque(numberOperations, methodAndValue))	
	