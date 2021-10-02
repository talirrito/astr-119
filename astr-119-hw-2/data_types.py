import numpy as np #imports the numpy library 
#integers 
#we will write everything in the highest level of program...
#snippet program, not going to use the best practices...what are the best practices?
i = 10 #integer 
print(type(i)) #this will print out the data type of i 

a_i = np.zeros(i,dtype=int) #length i, declare an array of ints, data type are integers. a_i is array of length i. 
print(type(a_i)) #will return ndarray (n-dimension array)
print(type(a_i[0])) #this will return int64, 64-bit-precision integer. 

#floats 
x = 119.0  #floating point number 
print(type(x)) #print out the type of x 

y = 1.19e2 #float 119 in scientific notation 
print(type(y)) #print out the type of y 

z = np.zeros(i, dtype=float) #declare an array of floats, can specify dtype=np.float64 or np.float32. 
print(type(z)) #print type of array 
print(type(z[0])) #float 