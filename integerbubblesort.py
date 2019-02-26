'''
check if an array at one element is greater than
the element after it, then move it to check against
the next array. If the array is not, then keep it
the same
'''

array = [4,5,1,20,19,23,21,6,9]

def bubbleSort (array):
	for i in range(len(array)):
		for j in range(0, len(array)-i-1):
			if array[j] > array[j+1]:
				array[j], array[j+1]= array[j+1], array[j]

bubbleSort(array)
for i in range(len(array)):
	print (array[i])

		

