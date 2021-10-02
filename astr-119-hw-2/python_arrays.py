x = [0.0, 3.0, 5.0, 2.5, 3.7] #define a list of numbers, an array 
print(type(x))

#print x
print("Originally x = ", x)

#remove the third element...oh no why??
x.pop(2) #list has a function called "pop" and that removes the value of that element. pop off based on index 
print(x)

#remove the element equal to 2.5
x.remove(2.5) #use .remove to remove a specific value 
print(x)

#get a copy 
y = x.copy() #this is a deep copy, so if I change y, it doesn't change x 
print(y)

#how many elements equal 0.0 
print(y.count(0.0))

#print the index with value 3.7 
print(y.index(3.7)) #if there's an element of y with vlaue 3.7, it will tell us the index of that element 

#sort the list into numerical order....default is smallest to largest? 
y.sort()
print(y)

#reverse sort 
y.reverse() #this reverses y in-place. it will be in reverse order. 
print(y)

#remove all elements 
y.clear()
print(y)