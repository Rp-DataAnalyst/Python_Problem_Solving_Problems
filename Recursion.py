# count = 0
# def example():
#  global count
#  count+=1
#  print(count)
#  example()

# example()



# count = 0
# def example():
#  global count
 
#  if count >=3:
#   return
#  count+=1
#  print(count)
#  example()

# example()


# def sample_function(n):
# 	if n < 1:
# 		return
# 	print(n)
# 	sample_function(n-1)
	

# sample_function(10)




# def sample_function(n):
# 	if n < 1:
# 		return
# 	print(n)
# 	sample_function(n-1)
# 	print(n)
	

# sample_function(10)


# def sample_function(n):
# 	if n < 1:
# 		return
# 	print(n)
# 	sample_function(n-1)
# 	print(n)
	

# sample_function(10)

#Factorial of a number:

# def factorial(n):
# 	if n == 1:
# 		return 1
# 	return n*factorial(n-1)

# print(factorial(5))

#sum of first n natural numbers:
# def sum_nnatural_numbers(n):
# 	if n == 1:
# 		return 1
# 	return n + sum_nnatural_numbers(n-1)

# print(sum_nnatural_numbers(5))  

# Sum_of_Digits_in_anumber:

# def sum_digits(n):
# 	if n < 10:
# 		return n 
# 	return n % 10 + sum_digits(n//10)

# print(sum_digits(1234))


#Reverse a string using recursion:

# def str_reversal(str1):
# 	if len(str1) == 1:
# 		return str1


# 	return str1[-1] + str_reversal(str1[:len(str1)-1])

# print(str_reversal("Ram Prasad"))



#Multiplication of a number using recursion:

# def mul_number(m,n):
# 	if n == 1:
# 		return m
# 	if n == 0:
# 		return 0
# 	return m + mul_number(m,n-1)

# print(mul_number(2,3))


#Exponential of a number:
def exponential_num(a,b):
	if b == 1 :
		return a
    return a * exponential_num(a,(b-1)



















