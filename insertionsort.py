'''
use the insertion sort algorithm to sort
through the array in ascending order
'''
array = [4,3,2,10,12,1,5,6]

def insertionSort (array):
	for i in range(len(array)):
		key = array[i]
		j = i-1
		while(j >= 0 and array[j] > key):
			array[j+1] = array[j]
			j = j-1
			array[j+1] = key
	return array		
					

print(insertionSort(array))				