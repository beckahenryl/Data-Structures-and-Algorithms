'''
given an array of characters, sort in order of appearance
'''
char = ['b','a', 'f', 'e','i', 'h']

def bubbleSortChar (char):
	for i in range (len(char)):
		for j in range(0, len(char)-i-1):
			if char[j] > char[j+1]:
				char[j], char[j+1] = char[j+1], char[j]


bubbleSortChar(char)

for i in range(len(char)):
	print (char[i])

