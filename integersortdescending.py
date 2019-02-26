'''
implement the sort algorithm in descending order
'''

array = [4,5,1,20,19,23,21,6,9]

def bubbleSort (array):
	for i in range(len(array)):
		for j in range(0, len(array)-i-1):
			if array[j] < array[j+1]:
				array[j+1], array[j]= array[j], array[j+1]

bubbleSort(array)
for i in range(len(array)):
	print (array[i])