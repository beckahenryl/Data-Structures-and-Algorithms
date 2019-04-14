array = [3, 50, 2, 5]
#        5  2  50  3

#start from last element and then go backwards in array, 
# move the last element to the first element's position- swapping the first and last elements
# after moving the last element to the first element's position, 

# 5 50 2 3
# swap the second to last element with the second element in the array
# 5 2 50 3

#return the swapped?

# 1th: 0 1 2
# 2th: 3 2 1

# 1th < 2th
# 1th ++
# 2th --

def reverseArray (array):
  lastPosition = len(array)-1 
  firstPosition = 0
  while (firstPosition < lastPosition): 
    array[firstPosition], array[lastPosition] = array[lastPosition], array[firstPosition]
    firstPosition += 1
    lastPosition = lastPosition - 1
  return array
  
  
    
print (reverseArray(array))
    
   # 5 50 2 3
    # 1th : 0 -> 1 -> 2 -> 3
    # 2th:  3 -> 2 -> 1 -> 0
    
    # 3 50 2 5
    # 3 2  50 5
    # 3 50 2  5
    # 5 50 2  3
    
    


