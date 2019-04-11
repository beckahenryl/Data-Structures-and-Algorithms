'''
IN PROGRESS-
4/11/2019- figure out what next step to take after following the 
first and second steps:

https://brilliant.org/wiki/sorting-algorithms/#sorting-algorithms

https://brilliant.org/wiki/merge/

Algorithm has two steps- sorting and merging
Divide and conquer method
Divide, Conquer, Combine

Merge Sort- how to merge two pre-sorted arrays such that the resulting
array is also sorted- can be implemented recursively or iteratively
'''

resultList = []

#presorted lists

A = [2,4,9]
B = [1,7,13,15]

def mergeList (A, B, resultList):
	for index in range (len(A)): #it is not enough to loop 3 times
		 #first step results [1], second step, results [1,2]
		if A[index] < B[index]:
			resultList.append(index)
			#get rid of value if it is in the resultList
			#so that I can work with the rest of the values
			#already existing. probably can only remove
			#the values in B
			for secondIndex in range(len(resultList)):
				if resultList[secondIndex] == B[secondIndex]:
				#delete 1 [7,13,15]
					del B[secondIndex]		
	return resultList		

print(mergeList(A,B,resultList))			
