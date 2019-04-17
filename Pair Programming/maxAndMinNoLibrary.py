#when you compare elements it is better than moving the location of the elements
# 0 1
array = [3, 50, 2, 5]
maximum = array[0] # 1
index = 0
indexForMin = 0
minimum = array[0]

#for i in range(len(presidents)):

for i in range(len(array)):
  temp = array[i]
  print ("-- temp: ", temp)# 50
  if temp > maximum:
    maximum = array[i]
    index = i
    print ("maximum: ", maximum)
    print ("index Maximum: ", index)
  if temp <  minimum:
    minimum = array[i]
    indexForMin = i
    print ("minimum: ", minimum)
    print ("index Minimum: ", indexForMin)
    
 
 
print ("Maximum: ", maximum)
print ("Max Index: ", index)
print ("Minimum: ", minimum)
print ("Min Index: ", indexForMin)

    
    # 1 2 10 3 7 6
    
    # max = 1 => 2 => 10
    
    # temp 2, 10
