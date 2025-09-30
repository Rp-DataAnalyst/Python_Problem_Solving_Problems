# def check_given_number(num1):
#       if num1>0:
#             return('The given number is a positive number')
#       elif num1==0:
#             return('The given number is a zero')
#       else:
#             return('The given number is a negative number')
# input_num1=int(input('enter a number'))
# res = check_given_number(input_num1)
# print(res)


# def check_number_status(num):
#       if num>0:
#             print('the given number is a positive number')
#       else:
#             if num==0:
#                   print('the given number is a zero')
#             else:
#                   print('the given number is a negative number')
# input_num = int(input('enter a nmber'))
# check_number_status(input_num)
# def even_or_odd(num1):
#       if num1%2==0:
#             print('Given number is a even number')
#       else:
#             print('Given number is a odd number')
# input_number=int(input('enter a number'))
# even_or_odd(input_number)
# def check_voter_eligibility_status(age):
#       if age>=18:
#             print('This person is eligible to vote')
#       else:
#             print('This person is a minor')
# input_age=int(input('enter your age'))
# check_voter_eligibility_status(input_age)
# Solving problem using ternary operator
# def even_or_odd(num1):
#       res= 'even' if num1%2==0 else 'odd'
#       print(res)
# even_or_odd(23)
# def check_voting_eligibility(age):
#       res = 'eligible to vote' if age>=18 else 'He is a minor'
#       print(res)
# check_voting_eligibility(99)
# def greatest_of_two_numbers(num1,num2):
#       return num1 if num1>num2 else num2

# res=greatest_of_two_numbers(233,45)
# print(res)
# fibanoci_numbers:
# n = int(input('enter a number:'))
# num1 = 5
# num2= 8
# for i in range(n):
#       print(num1)
#       third_number = num1+num2
#       num1=num2
#       num2=third_number
# from functools import reduce
# list1 = [2,55,68,98,34]
# max_number= reduce(lambda x,y: x if x>y else y,list1)
# print(max_number)
# n = int(input('enter a number:'))
# num1=0
# num2=2
# for i in range(n):
#       print(num1)
#       num1,num2 = num2,num1+num2
# fibonacci numbers:
# def fibonacci(n):
#       a,b=0,1
#       for i in range(n):
#             print(a,end=" ")
#             a,b=b,a+b
# fibonacci(10)
#armstrong numbers:
# n = (input('enter a number:'))
# power = len(n)
# num = int(n)
# original_num = num
# sum_of_powers=0
# while num >0:
#      digit= num%10
#      sum_of_powers+=digit**power
#      num//=10

# if original_num == sum_of_powers:
#      print('The given number is armstrong ')
# else:
#      print('The given number is not a armstrong number')
# def pass_or_fail(marks):
#       if marks>40:
#             print('The student is passed')
#       else:
#             print('The student was failed')
# pass_or_fail(3)
# num=int(input('enter a number:'))
# if num>7:
#       print('You are entered a wrong number')
# elif num ==1:
#       print('Monday')
# elif num==2:
#       print('Tues Day')
# elif num==3:
#       print('Wedenesday')
# elif num==4:
#       print('Thursday')
# elif num==5:
#       print('Friday')
# elif num==6:
#       print('Saturday')
# else:
#       print('Sunday')
# def day_of_week(num):
#       days={
#             1: 'Monday',
#             2: 'Tuesday',
#             3: 'Wednesday',
#             4: 'Thursday',
#             5: 'Friday',
#             6: 'Saturday',
#             7: 'Sunday'

#       }
#       return days.get(num,'You have entered the invalid number. please enter the number between 1-7')
# num=int(input('enter a number:'))
# print(day_of_week(num))
# def calculator(a,b):
#       print('addition', a+b)
#       print('Substraction', a-b)
#       print( 'Multiplication', a*b)
#       if b!=0:
#             print( 'Division', a/b)
#       else:
#             print('division by zero is not possible')
# calculator(3,4)
# def calculator():
#     print("Simple Calculator")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")

#     choice = int(input("Enter choice (1-4): "))

#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))

#     if choice == 1:
#         print("Result =", a + b)
#     elif choice == 2:
#         print("Result =", a - b)
#     elif choice == 3:
#         print("Result =", a * b)
#     elif choice == 4:
#         if b != 0:
#             print("Result =", a / b)
#         else:
#             print("Error: Cannot divide by zero")
#     else:
#         print("Invalid choice!")

# # Run the calculator
# calculator()
# character = input("Enter a character: ").lower()

# def vowel_consonant_neither(ch):
#     if ch.isalpha():   # check if it's a letter
#         if ch in ('a', 'e', 'i', 'o', 'u'):
#             print("The given character is a vowel")
#         else:
#             print("The given character is a consonant")
#     else:
#         print("The given character is neither vowel nor consonant")

# vowel_consonant_neither(character)

# def students_grade(marks):
#       if marks>100:
#             print('You have entered wrong marks. Please enter values between 1 - 100')
#       else:
      
#             if marks <=100 and marks>=90:
#                   print('The student grade is A')
#             elif marks >=80:
#                   print('The student grade is B')
#             elif marks >=70:
#                   print('The student grade is C')
#             else:
#                   print('The student is failed')
# students_grade(70)
# def check_triangle(a,b,c):
#       if a+b>c and b+c>a and c+a>b:
#             print('The given three lengths can form a triangle')
#             if a==b==c:
#                   print('The given triangle is Equilateral Triangle')
#             elif a==b or b==c or c==a:
#                   print('The given triangle is Isosceles triangle')
#             else:
#                   print('The given traingle is Scalene triangle')

#       else:
#             print('The triangle can not be formed')
# check_triangle(2,5,6)
#loop questions:
#Print all numbers from 1 to 100 using a for loop. 
# for i in range(2,101,2):
#       print(i, end=',')
# i=1
# while i<101:
#       print(i, end=" ")
#       i+=1
#Write a program to print the sum of the first n natural numbers. (n*n+1/ 2) 
# sum_of_first_nnaturalnumbers=0
# for i in range(1,11):
#       sum_of_first_nnaturalnumbers+=i
# print(sum_of_first_nnaturalnumbers)
#Print all even numbers between 1 and 50 using a while loop. 
# i=1
# while i<51:
      
#       if i%2==0:
#             print(i, end=" ")
#       i+=1
#Write a program to display the multiplication table of a given number. First 20
# for j in range(1,21):

#       for i in range(1,11):
#             print(j,'*',i,'=',j*i)
#Reverse a number using a while loop. Also can we get the sum of all the digits.

# num = int(input('enter a number:'))
# reverse=0
# sum_of_digits=0
# n=num
# while n>0:
#       digit=n%10
#       reverse=reverse*10+digit
#       sum_of_digits+=digit
#       n=n//10
# print(reverse)
# print(sum_of_digits)
#Write a program to count the number of digits in a given number using a while loop.
# num = int(input('enter a number:'))
# count=0
# while num>0:
#       digit=num%10
#       count+=1
#       num =num//10
# print(count)
# num=int(input('enter a number:'))
# reverse=0
# sum_of_digits=0
# n=num
# while n>0:
#       digits=n%10
#       reverse=reverse*10+digits
#       sum_of_digits+=digits
#       n=n//10
# print(reverse)
# print(sum_of_digits)
# num = int(input('enter a number:'))
# reverse= int(str(num)[::-1])
# sum_of_digits=sum(map(int,str(num)))
# print(reverse)
# print(sum_of_digits)
# num=int(input('enter a number:'))
# reverse=''
# sum_of_digits=0
# for chr in str(num):
#       sum_of_digits+=int(chr)
#       reverse=chr+reverse
# print('the reversed number:',int(reverse))
# print('the sum of digits',sum_of_digits)
# num = int(input("Enter a number: "))

# reverse = ""
# sum_of_digits = 0

# for ch in str(num):
#     sum_of_digits += int(ch)
#     reverse = ch + reverse   # build reverse manually

# print("Reversed number:", int(reverse))
# print("Sum of digits:", sum_of_digits)
#Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a while loop. 
# num1=int(input('enter a number:'))
# while num1>0:
#       print('You are entered the number:',num1)
#       num1=int(input('enter  a number:'))
# print('you are entered the negative number')
#Print the first 10 terms of the Fibonacci series using a for loop. 
# num1=0
# num2=1
# n=10
# # for i in range(n):
# #       print(num1)
# #       num1,num2=num2,num1+num2
# for i in range(n):
#       if i==n-1:
#             print(num1)
#       else:
#             print(num1,end=",")
#             third_num=num1+num2
#             num1=num2
#             num2=third_num
# num1 = 0
# num2 = 1
# n = 10
# fib = []

# for i in range(n):
#     fib.append(str(num1))
#     third_num = num1 + num2
#     num1 = num2
#     num2 = third_num

# print(",".join(fib))
#Check if a given number is a prime number using a for loop. 
# num= int(input('enter a number:'))
# if num<2:
#       print('You have entered invalid number')

# else:  
#       is_prime=True     
#       for i in range(2,int(num*.5)+1):
#             if num%i==0:
#              is_prime=False
#              break
#       if is_prime:
#             print('The given number is prime')
#       else:
#             print('The given number is not a prime number')
#Write a program to calculate the factorial of a number using a while loop. 
# factorial=1
# n=1
# while n<=5:
#       factorial*=n
#       n+=1
# print(factorial)
#Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i,end=' ')
# Implement a menu-driven program where the user can choose to:
# Find the square of a number. 
# Find the cube of a number. 
# Exit.

# while True:
#       print('\n Menu')
#       print('1. Find the square')
#       print('2.Find the cube:')
#       print('3. Exit')

#       choice = int(input('enter your choice (1/2/3):'))
#       if choice==1:
#             num=int(input('enter a number:'))
#             print(f"The square of a given {num}={num**2}")
#       elif choice==2:
#             num=int(input('enter a number:'))

#             print(f"The cube of a given {num}={num**3}")
#       elif choice==3:
#             print('Exiting the programm .... Goodbye!')
#             break
#       else:
#             print('Invalid choice! Please select 1,2, or 3')
#Implement a basic login system where the user has three attempts to enter the correct password using a loop. 
# correct_password= 'Ram@7330'
# attempts=3
# while attempts>0:
#       enter_password=input('enter your password:')
#       if enter_password==correct_password:
#             print('Login successful. Welcome!!')
#       else:
#             attempts-=1
#             if attempts>0:
#                   print(f'you have entered the wrong password, still  {attempts} attempts remained.')
#             else:  
#                   print('Your attempts are over, Your account has been blocked')
#Number Questions:
# number= input('enter a number')
# print(int(number[::-1]))
#4)Reverse a Number


# def reversed_number(n):
#       reverse=0
#       while n>0:
#             digit=n%10
#             reverse=reverse*10+digit
#             n=n//10
#       print(reverse)


# reversed_number(231)
#6)Fibonacci series
# num1=0
# num2=1
# n=10
# for i in range(n):
#       print(num1,end=' ')
#       num1,num2=num2,num1+num2
# def fibonacci_series(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# # Example
# num = int(input("Enter how many terms you want in Fibonacci series: "))
# fibonacci_series(num)
#fibonacci_series Nth term:
# def fibonacci_Nthterm(n):
#       a,b=0,1
#       if n==1:
#             return a
#       elif n==2:
#             return b
#       for i in range(3,n+1):
#             a,b=b,a+b
#       return b
# n = int(input('enter a number:'))
# print(f"The fibonacci {n}th term is:{fibonacci_Nthterm(n)}")
#5) Palindrome Number
# num= int(input('enter a  number:'))
# original=num
# reverse=0
# while num>0:  
#       digit=num%10
#       reverse=reverse*10+digit
#       num=num//10
# print(reverse)
# if original== reverse:
#       print('The given number is a palindrome number')
# else:
#       print('The given number is not a palindrome number')
# Perfect Number:
# num= int(input('enter a number:'))
# original=num
# sum=0
# for i in range(1,num//2+1):
#       if num%i==0:
#             sum+=i
# sum-=original
# print(sum)
# if original==sum:
#       print('The given number is a perfect number')
# else:
#       print('The given number is not a perfect number') 
# write a programm to print the fibonacci series based on the user input
# a= int(input('enter  starting number of fibonacci series:'))
# b= int(input('enter second number of fibonacci series:'))
# n=int(input('no of terms fibonacci series required'))
# for i in range(n):
#       print(a)
#       a,b=b,a+b
# Wap to print the non-Fibonacci numbers by the given input
# n= int(input('enter a number:'))
# fib1,fib2=0,1
# fibs=set()
# while fib1<=n:
#       fibs.add(fib1)
#       fib1,fib2=fib2,fib1+fib2
# print('The non-fibonacci numbers upto',n,'are:')
# for i in range(1,n+1):
#       if i not in fibs:
#             print(i,end=' ')
#11) Wap to print nth non -Fibonacci number. {input : 10  Output : 16}
# Loop Questions:
# for i in range(1,11):
#       if i==10:
#             print(i)
#       else:
      
#             print(i,end=' ,')
# n=10
# while n>0:
#       if n==1:
#             print(n)
#       else:
#             print(n,end=',')
#       n-=1
#2)Wap to print 10 to 1 without using greater than or less than operator
# for i in range(10,0,-1):
#       print(i,end=' ')
#3) Wap to print -1 to -10 without using greater than symbol
# for i in range(-1,-11,-1):
#       print(i, end=' ')
# i=-1
# while i!=-11:
#       print(i,end=' ')
#       i-=1
# for i in range(-10,0,1):
#       print(i,end=' ')
# i=-10
# while i<0:
#       print(i,end=' ')
#       i+=1
#4) Wap to print sum of digits in a number. {input:123  output: 6}
# num1= int(input('enter a number:'))
# sum=0
# while num1>0:
#       digit= num1%10
#       sum+=digit
#       num1=num1//10
# print(sum)
#5) Wap Sum of Even Numbers
# num1= int(input('enter a number:'))
# sum=0
# while num1>0:
#        digit= num1%10
#        if digit%2==0:
#             sum+=digit
#        num1=num1//10
# print(sum)
#6) Wap to print whether a given number is prime or not prime. But need to check 1 also
# num1= int(input('enter a number:'))
# if num1==1:
#       print('The given number is not  a prime number')
# elif num1>1:
#       is_prime = True
#       for i in range(2,num1):
#             if num1%i==0:
#                   is_prime=False
#                   break  
#       if is_prime:
#                   print('The given number is a prime number')
#       else:
#                   print('The given number is not a prime number')
# else:
#       print('You are entered invalid number.') 
#7) Print prime numbers up to a given number && Wap to print the prime number between 1-100
# num1= int(input('enter a number:'))
# print('Prime numbers upto given',num1,'are:')
# for num in range(2,num1+1):
#       is_prime=True
#       for i  in range(2,int(num**.5)+1):
#             if num%i==0:
#                   is_prime=False
#                   break 
#       if is_prime:
#                   print(num, end=' ')
#Wap to print the prime number between 1-100
# first_number=int(input('enter the first number:'))
# last_number=int(input('enter the last number:'))
# print('the prime numbers between ',first_number,'-',last_number,'are:')
# for num in range(first_number,last_number+1):
#       if num>1:

#             is_prime=True
#             for i in range(2,int(num**.5)+1):
#                   if num%i==0:
#                         is_prime=False
#                         break
#             if is_prime:
#                   print(num,end=' ')
#8)Wap to print sum of non-primes in a number. {input:3436 output -10}
# num1= (input('enter a number:'))
# sum=0
# for digit in str(num1):
#       d=int(digit)
#       if d not in [2,3,5,7]:
#             sum+=d 
# print('The sum of non-primes in a number are:',sum)
# num1= int(input('enter a number:'))
# sum=0
# while num1>0:
#       digit= num1%10
#       if digit not in [2,3,5,7]:
#             sum+=digit
#       num1=num1//10
# print(f'The sum of non-primes in a number are {sum}')
# 9) Wap to print the sum of odd digits in a number. { input : 2355 output : 13}
# num1=int(input('enter a number:'))
# sum=0
# while num1>0:
#       digit=num1%10
#       if digit%2!=0:
#             sum+=digit
#       num1=num1//10
# print(sum)
# def is_prime(n):
#       if n<2:
#             return False 
#       c=0
      
#       for i in range(1, n+1):
#             if n%i==0:
#                   c+=1
#       if c==2:
#             return True
#       return False 
            
                   
# print( is_prime(3))

# print next prime number:
# def is_prime(n):
#       if n<2:
#             return False
#       for i in range(2,n+1):
#             if n%i==0:
#                   return False
#       return True
# n = int(input('enter a number'))
# if is_prime(n): 
#       print(n)
# else:
#       while True:
#             n+=1
#             if is_prime(n):
#                   print(n)
#                   break 
# a,b,c=3,1,2
# if a<=b and a<=c:
#       print(b+c)
# elif b<=a and b<=c:
#       print(a+c)
# else:
#       print(a+b)
#10) Wap to check whether a number is prime or not by using a function.
# Additional print a prime numbers up to 20.
# def is_prime(n):
#       if n <2:
#             return False
#       for i in range(2,int(n**.5)+1):
#             if n%i==0:
#                   return False
#       return True

# num= int(input('enter a number:'))
      
# if is_prime(num):
#       print(f'The given number {num} is a prime number ')
# else:
#       print(f'The given number {num} is not a prime numbers ')
# print('Prime Numbers upto 15')
# for number in range(1,num+1):
#       if is_prime(number):
#             print(number, end= ' ')
# Take a number and check if it is a armstrong number or not
# num = int(input('enter a number:'))
# tem= num
# sum_of_digits=0
# power= len(str(num))
# while num>0:
#       digit= num%10
#       digits_exp=digit**power
#       sum_of_digits+=digits_exp
#       num=num//10
# print('sum_of_digits',sum_of_digits)
# if sum_of_digits==tem:
#       print('The given number is a armstrong number') 
# else:
#       print('The given number is not a armstrong number')

#12)Amstrong Number in a given range
# def check_Armstrong(n):
#       temp=n
#       sum_of_digits=0
#       power= len(str(n))
#       while n>0:
#             digit= n%10
#             digits_exp=digit**power
#             sum_of_digits+=digits_exp
#             n=n//10
#       return sum_of_digits==temp
      
 
# n1=int(input('enter the starting range num'))
# n2= int(input('enter the ending num range'))
# for i in range(n1,n2+1):
#       if check_Armstrong(i):
#             print(i, end=' ')
# check a armstrong number and finding out no of digits in a number without length function
# num = int(input("Enter a number: "))
# temp = num
# sum_of_digits = 0

# count digits without len()
# power = 0
# temp2 = num
# while temp2 > 0:
#     power += 1
#     temp2 //= 10

# calculate sum of digits raised to power
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum_of_digits += digit ** power
#     temp //= 10

# check Armstrong
# if sum_of_digits == num:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is NOT an Armstrong number")
# n1= int(input('enter a number:'))
# lst1=[]
# temp=n1
# while n1>0:
#       digit=n1%10
#       lst1.append(digit)
#       n1//=10
# print(lst1.reverse())
# max_value=max(lst1)
# min_value = min(lst1)
# max_index= lst1.index(max_value)
# min_index=min.inlst1(min_value)
# if min_index< max_index:
#       print('min index is first')
# else:
#       print('max index is first')
#14) Wap to print the minimum prime digit in a number
# n1= int(input('enter  a number:'))
# prime_numbers=[2,3,5,7]
# prime_digits=[]
# while n1>0:
#       digit=n1%10
#       if digit in prime_numbers:
#             prime_digits.append(digit)
#       n1//=10
# prime_digits.sort()
# if prime_digits:
#       print('The smallest prime number in the given number is:',prime_digits[0])
# else:
#       print('No prime digits were found in the number.')
#15) Wap to print nearest prime number to the given input
 
# def is_prime(n):
#       if n<2:
#             return False
#       for i in range(2,int(n**0.5)+1):
#             if n%i==0:
#                   return False
#                   break
#       return True
# def nearest_prime(n): 
#       d=1
#       while True:
#             if (n-d>=2) and is_prime(n-d):
#                   return n-d
#             if is_prime(n+d):
#                   return n+d 
#             d+=1

# num1= int(input('enter a numebr:'))
# print('The nearest prime number for the given number is ',nearest_prime(num1))
#list/Array Problems:
#Sum of elements in a list:
# list1=[1,2,4,8]
# sum=0
# for i in list1:
#       sum+=i
# print(sum)
#2)Finding the k Element which is present in a List.
# list1=[2,3,4,5]
# k=int(input('enter a number:'))
# if len(list1) ==0:
#       print('The list is empty')) 
# elif k<1 or k>len(list1):
#        print("you are entered invalid number please enter between 1 and ",len(list1))
# else:
#        print('The k element value is ',list1[k-1])
# list1 = list(map(int, input("Enter numbers separated by space: ").split(',')))
 
# print(list1)
#Printing k element from right side
# list2=[2,3,4,5]
# k= int(input('enter a number:'))
# if len(list2)==0:
#       print('The list is empty.')
# elif k<0 or k>(len(list2)):
#       print('The k value is invalid')
# else:
#       print(list2[-k])
# Reverse right angle Patterns:
# for i in range(5):
#       for j in range(5-i):
#             print('*',end=' ')
#       print()
#Right angle pattern:
# for i in range(5):
#       for j in range(i+1):
#             print('*',end=' ')
#       print()
# right aligned triangle
# n = 5
# for i in range(1, n+1):
#     # print spaces first
#       print(" " * (n - i), end="")   # for printing  the spaces
#     # then print the $ symbols
#       print("$" * i)
# num=1
# for i in range(1,5):
#       for j in range(i):
            
#             print(num,end= ' ')
#             num+=1
#       print()
#sequence of numbers:
# n=6
# num=1

# for i in range(1,n+1):
#       row_numbers=[]
      
#       for j in range(i):
#             row_numbers.append(num)
            
#             num+=1
#       if i%2==0:
#             row_numbers.reverse()
#       print(" ".join(map(str, row_numbers)))
"""
This program prints a number triangle based on a given number of rows (N).
The numbers are continuous across all rows.
- Odd-numbered rows display non-prime numbers in ascending order.
- Even-numbered rows display non-prime numbers in descending order.
"""

# def is_prime(n):
#     """
#     Checks if a number is prime.
#     A prime number is a natural number greater than 1 that has no positive
#     divisors other than 1 and itself.
#     """
#     if n <= 1:
#         return False
#     # Check for divisors from 2 up to the square root of n
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def print_triangle(N):
#     #Generates and prints a number triangle for N rows with continuous numbers.

#     # Calculate the total number of non-prime numbers needed for the entire triangle.
#     total_needed = N * (N + 1) // 2

#     # Pre-generate a list of all non-prime numbers required.
#     all_non_primes = []
#     current_num = 1
#     while len(all_non_primes) < total_needed:
#         if not is_prime(current_num):
#             all_non_primes.append(current_num)
#         current_num += 1

#     # Use an index to track which numbers have been used in the triangle.
#     start_index = 0

#     # Iterate through each row to print the numbers.
#     for row in range(1, N + 1):
#         # Determine the end index for the current row's numbers.
#         end_index = start_index + row

#         # Slice the non-prime numbers for the current row from the master list.
#         row_numbers = all_non_primes[start_index:end_index]

#         # Determine the order based on the row number.
#         if row % 2 == 0:
#             # Even rows: print descending
#             row_numbers.reverse()
#         # Odd rows are already in ascending order

#         # Print the numbers for the current row, separated by spaces.
#         print(' '.join(map(str, row_numbers)))

#         # Update the start index for the next row.
#         start_index = end_index

# # Example usage for N=5
# print_triangle(5)
#Method:1
# list1=['a','e','i','o','u']
# list2=[]
# for char in list1:  
#       list2.insert(0,char)
# print(list2)
#Task use all methods used to reverse a string 
# [12,34,63] find sum of digits of each element in list
# 123 find max digit in a list
#find max digit for every num in the given list
# def sum_of_digits(n):
#       sum=0
#       while n>0:
#             digit=n%10
#             sum+=digit
#             n//=10
#       return sum
# # num1= int(input('enter a number:'))
# list1=[234,432,532]
# for i in list1:
#       print(sum_of_digits(i),end=' ')
#2)Finding the k Element which is present in a List.


# def k_element(list1,k):
#       list1.sort()
#       if k < 0 or k > len(list1):
#             return 'invalid k value'
#       return list1[k-1]
# list1 = [2,3,4,5,33,6]
# k_value = 4
# print(k_element(list1,k_value))
#3Wap to print duplicates and unique numbers in an array/List.
# def find_duplicates_unique_values(input_list):
#     unique_values = []
#     duplicate_values = []
#     count = []
#     for num in input_list:
#         count = input_list.count(num)
#         if count>1 and num not in duplicate_values:
#             duplicate_values.append(num)
        
#         elif count == 1:
#             unique_values.append(num)
#     print('duplicate_values',duplicate_values)
#     print('unique_values', unique_values)
# list1 = [1,2,3,4,5,3,4,6,7,8]
# find_duplicates_unique_values(list1)






# def find_duplicates_unique_values(input_list):
#     unique_values = []
#     duplicate_values = []
#     for num in input_list:
        
#         count = input_list.count(num)
#         if count>1 and num not in duplicate_values:
#             duplicate_values.append(num)
        
#         elif count == 1:
#             unique_values.append(num)
         
#     print('duplicate_values',duplicate_values)
#     print('unique_values', unique_values)




# list1 = [1,2,3,4,5,3,4,6,7,8]
# find_duplicates_unique_values(list1)

#Wap that takes an array of integers as input and calculates the sum of the digits of each number in the list.
# Input: [202,89,112,88]   Output: [4,17,14,6]

# def sum_of_digits (list1):
#     Result = []
    
#     for num in list1:
#         Total = 0
#         while num >0 :
#             digit = num%10 
#             Total += digit
#             num//=10
#         Result.append(Total)
#     return Result


# list1 = [ 12,345,546,485,34]
# print(sum_of_digits(list1))

# import math
# def sum_of_digits(list2):
#     return[sum(digits(num) for num in list2)]

#5)  WAP to Count Occurrences of Each Digit in a list.

 
            

#Today's assignment:

#Wap to check if each number in an  list contains duplicate digits, returning true for duplicates and false for unique digits.
#Input: [202,89,112,88]       	Output:[true ,false ,true ,true]


# def check_duplicate_element(list1):
#     result = []

#     for num in list1 :
#         num_str = str(num)
#         has_duplicate = False 
#         for digit in num_str:
#             if num_str.count(digit) > 1 :
#                 has_duplicate = True
#                 break
#         result.append(has_duplicate)
#     print(result)
# numbers = [202,89,112,88] 
# check_duplicate_element(numbers)

# for i in range(5):
#         for j in range(5-i):
#                 print('*',end=' ')
#         print()


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def print_triangle(N):
#     num = 1  # start number
#     for row in range(1, N+1):
#         row_vals = []
#         while len(row_vals) < row:
#             if not is_prime(num):   # skip primes
#                 row_vals.append(num)
#             num += 1
#         if row % 2 == 0:   # even row → ascending
#             print(" ".join(map(str, row_vals)))
#         else:              # odd row → descending
#             print(" ".join(map(str, row_vals[::-1])))

# # Example
# print_triangle(5)


for i in range(5):
	for j in range(5-i):
		print(j,end=" ")
	print()

















          



# list1 = [12,45,34,25,86,333,322]

    






 











  




      

      



      


       




                  
            

      
            
      



      






 






 



            
       

















      











      
















            
 






