arry = [100,25,2,30]

def findMinimum (arry):
	arry.sort() #sort through array
	return arry[0] #first element will be minimum

print ("Minimum: ", findMinimum(arry))

def findMaximum (arry):
	arry.sort() #sort through the array
	return arry[-1] #last element will be maximum

print ("Maximum: ", findMaximum(arry))					
