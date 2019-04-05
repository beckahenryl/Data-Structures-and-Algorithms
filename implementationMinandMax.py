#solution built from sort implementation

arry = [100,25,2,30]

def bubbleSort (arry):
	for i in range(len(arry)):
		for j in range(0, len(arry)-i-1):
			if arry[j] > arry[j+1]:
				arry[j], arry[j+1]= arry[j+1], arry[j]


def findMinAndMaxImplementation(arry):
	bubbleSort(arry)
	return arry[0], arry[-1]

print ("Sorted: ", findMinAndMaxImplementation(arry))