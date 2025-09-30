#Recursion_Assignment 26-09-2025:

#1Q: Print first N natural numbers using recursion:

 
def natural_numbers(n):
    if n < 1:
        return
    natural_numbers(n-1)   # recursive call first
    print(n)               # print after recursion

natural_numbers(10)


#3) First N even numbers using recursion:

def even_numbers(n):
    if n < 0:
        return
    even_numbers(n-2)
    print(n)
even_numbers(10)
 





#2  N natural numbers using recursion in reverse order:

def natural_numbers_reverse(n):
	if n < 1:
		return 
	print(n)
	natural_numbers_reverse(n-1)

(natural_numbers_reverse(10))