numberOperations = int(input())

methodAndValue = []


#get method and value, store into list
for i in range (0, numberOperations):
	i = input()
	methodAndValue.append(i)


def pythonLists (numberOperations, methodAndValue):

	performOperation = []
	emptyListForChanges = []

	#split the values within original list to separate
	#the string method from the integer value

	for index in methodAndValue:
		performOperation.append(index.split())

	for i in performOperation:
		if i[0] == 'insert': #takes index and element
			emptyListForChanges.insert(int (i[1]), int (i[2]))
		if i[0] == 'print':
			print (emptyListForChanges)
		if i[0] == 'remove':
			emptyListForChanges.remove(int (i[1]))
		if i[0] == 'append':
			emptyListForChanges.append(int (i[1]))
		if i[0] == 'sort':
			emptyListForChanges.sort()
		if i[0] == 'pop':
			emptyListForChanges.pop()
		if i[0] == 'reverse':
			emptyListForChanges.reverse()
	return ''								

print (pythonLists(numberOperations, methodAndValue))	
	