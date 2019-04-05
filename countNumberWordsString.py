string = "I am awesome"

def countNumberWords (string):
	#string.split() split into list so that I can count using len
	return len(string.split())
print ("Number of Words: ", countNumberWords(string))	
