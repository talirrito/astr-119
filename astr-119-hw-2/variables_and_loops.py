import numpy as np  #we use numpy for many things! 


def main():

	i = 0  # i is an integer, declared with  number 0
	n = 10 # n is another integer 
	x = 119.0 #floating point numbers are declared with a .

	# we can use numpy to declare arrays quickly 


	y = np.zeros(n, dtype=float) 


	# we can use for loops to iterate with a variable 

	for i in range(n):  # i in range [0, n-1]
		y[i] = 2.0 * float(i) + 1.0 #set y = 2*i+1 as floats 
		#so this is the odd numbers...MY OWN NOTE. 

	# we can simply iterate through a variable array 
	for y_element in y: 
		print(y_element) 
		#this is printing out every element of y in sequence. 

#execute the main function 
if __name__=="__main__":
	main()