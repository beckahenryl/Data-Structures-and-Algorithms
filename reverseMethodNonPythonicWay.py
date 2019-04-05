#reverse it using a new array
#contrary to the file name, this is very pythonic
arrayToReverse = [21,98,77,24]

def reversalPythonicWay (arrayToReverse):
	newArray = []
	for i in range (0, len (arrayToReverse)):
		newArray.append(arrayToReverse[-1]) #access last element and add to new array
		arrayToReverse.pop() #remove the last element
	return newArray

print ("Reversed Array: ", reversalPythonicWay(arrayToReverse))		
