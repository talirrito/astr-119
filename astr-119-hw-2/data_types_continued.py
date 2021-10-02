#string 

s = "I am a string."
print(type(s))  #returns str 

#Boolean ...these are specifically true or false. NO possibility you would have the wrong precision. 

yes = True 	#Boolean True, "True" is a protected term in python 
print(type(yes)) #boolean 

no = False 
print(type(no)) 

#List -- ordered and changeable 
alpha_list = ["a", "b", "c"] #list intialization 
print(type(alpha_list))   #will say tuple 
print(type(alpha_list[0])) #will say string...I originally missed a parenthesis here and it messed up my whole code! 
alpha_list.append("d")    #will add "d" to the end of the list 
print(alpha_list)

#Tuple -- ordered and unchangeable 

alpha_tuple = ("a", "b", "c") #tuple intialization 
print(type(alpha_tuple)) #will say tuple 

try: 
	alpha_tuple[2] = "d"
except TypeError:
		print("We can't add elements to tuple!") 
print(alpha_tuple)