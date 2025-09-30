#Given a list where each element represents the color of a sock, e.g., ['red', 'green', 'red', 'purple', 'green', 'black', 'red'], 
# how many days can I sustain if I can wear only one matching pair of socks per day
#  and each pair can be used only once?"

def matching_pairs(list1):
	#Method 1 for getting dictionary	
	dict1 = {}
	for el in list1:
		if el not in dict1:
			dict1[el] = 1 
		else:
			dict1[el] +=1
	print('counts', dict1)
	for key,value in dict1.items():
		if value > 1 :
			print(f"element {key} occurs {value} times")
list1 = [12,34,45,34,76,67,76,12]
matching_pairs(list1)

#Medthod:2 for getting dictionary from list:

list2 = [12,34,45,34,76,67,76,12]
dict2 = []
for i in list2:
	dict2[i] =  



		