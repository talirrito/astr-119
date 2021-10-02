#define a dictionary data structure 
#dictionaries are lists but with key value associations 
#dictionaries have a key : value for the elements, like looking up a word in the dictionary 
#in astronomy, will often depict catalogues as dictionary. difficult to use arrays instead of this. 
example_dict = { 
	"class" : "Astr 119",
	"prof" : "Brant", 
	"awesomeness" : 10 #note that the last element does NOT have a comma 
}
print(type(example_dict)) # will say dict 

#get a value via a key 
course = example_dict["class"] #this will replace class" with "course
print(course)

#change a value via a key 
example_dict["awesomeness"] += 1 #increase awesomeness 

#print dictionary 
print(example_dict) 

#print dictionary element by element 
for x in example_dict.keys(): #x equals to first key, 2nd, 3rd. print that key then print the value associated with that key. 
	print(x, example_dict[x]) 