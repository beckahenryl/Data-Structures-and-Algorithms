ReverseList = [1,4,3,2]

def implementReverseMethod (ReverseList):
	emptyListAppend = []
	for i in ReverseList[::-1]:
		emptyListAppend.append(i)
	return emptyListAppend

print (implementReverseMethod(ReverseList))