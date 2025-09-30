# 2.Print exponent of two numbers without using double star operator & loops

def exponential_nums(a,b):
	if b == 1 or 0 :
		return a
	return a * exponential_nums(a,b-1)

print(exponential_nums(2,3))



# 1.Print list in a reverse order 


def rev_list_elements(list1):

	if len(list1)==1:
		return list1
	
	return [list1[-1]] + rev_list_elements(list1[:len(list1)-1])

print(rev_list_elements([12,23,45,67]))
 