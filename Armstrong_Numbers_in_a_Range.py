starting_range = int(input('enter a initial number '))
ending_range = int(input('enter final number'))
for num in range(starting_range,ending_range+1):
      digits=0
      sum_of_powers = 0
      temp = num
      while temp>0: #for getting no of digits in a number
           
            digits+=1
            temp//=10


      temp = num
      while temp>0:
            digit = temp%10
            sum_of_powers+=digit**digits
            temp//=10

      if sum_of_powers==num:
            print(num,'This is armstrong number')
      


      #Finding prime numbers in a given range:
initial_range = int(input("Enter first number range: "))
final_range = int(input("Enter final number range: "))

for num in range(initial_range, final_range + 1):
    if num < 2:
        print(num, "is not a prime number")
    else:
        s = 0
        for i in range(2, num ):  # start from 1
            if num % i == 0:
                s += 1
        if s == 2:  # only divisible by 1 and itself
            print(num, "is a prime number")
        else:
            print(num, "is not a prime number")

            
 

            
