# startingPoint = 3, numElementsToShift = 2
# arr[1] = arr[3]
# arr[2] = arr[4]
# shift element at position  startingPoint to the left by numElementsToShift
# arr[] = arr[startingPoint]

# arr[2] = arr[4]

#shift elements left




array = [1,2,2,2,3,4,5,6] #4 -> (4-3) 
#       [1,2,3,2,3]

# I check for duplicates, if there are duplicates, I count the number of elements until there are no dulpicates- create a count variable
# i 
# i + 1

count = 0
startingPosition = 0
for i in range(startingPosition, len(array)-1):
  if (array[i] == array[i+1]): #next element
    count += 1 #returns number of duplicates
  else:
    if count != 0:
      startingPosition = i+1 # check if count != 0, next element after last duplicate
      break #because you found the duplicate

def shiftElements(array, startingPosition, count):
  # start from startingPoint to the last element
  for i in range(startingPosition, len(array)):
    array[i - count] = array[i] #subtract the starting point from number of elements to shift- first iteration
  return array

#without duplicates, this would be the length of the array
print (len(array) - count)

print (shiftElements(array, startingPosition, count))

# 1 2 3 3 4 5

#shiftElements(array,)
# after the count = 3, 3 + 1 = 4 shift by one element to get that start position


