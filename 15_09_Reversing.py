#Reverse elements in list1:
#Method:1
# list1=[23,55,64,-54]
# new_list= list1.reverse()
# print(list1)
#Method:2
# list1=[23,55,64,-54]
# reversed_list=list1[::-1]
# print(reversed_list)
#Method:3
# def reverse(input_list):
#       reversed_list=[]
#       for i in input_list:
#             reversed_list.insert(0,i)
#       return reversed_list

# list1=[23,55,64,-54]
# print(reverse(list1))
#Method:4
# list1=[23,55,64,-54]
# new_list=[]
# for i in list1:
#       new_list.append(i)

# print(new_list)
#efficient way
# list1=[23,55,64,-54]
# low = 0
# high= len(list1)-1
# while low<high:
#       list1[low],list1[high] = list1[high], list1[low]
#       low+=1
#       high-=1
# print(list1)
#reversing half of a list items:
# list1=[23,55,64,-54]
# low=0
# high=(len(list1)-1)//2
# while low<high:
#       list1[low],list1[high] = list1[high],list1[low]

#       low+=1
#       high-=1
# print(list1)
# Define the list of numbers.


# This function calculates the sum of all digits of each element in a list.
def sum_digits(input_list):
    # Initialize a variable to store the final sum of all digits.
    total_sum_of_digits = 0
    
    # Iterate through each number in the input list.
    for number in input_list:
        # Use abs() to handle negative numbers, as the digit summing logic works with positive integers.
        current_number = abs(number)
        
        # Use a while loop to extract and sum the digits of the current number.
        while current_number > 0:
            # Get the last digit of the number using the modulo operator.
            digit = current_number % 10
            # Add the digit to the running total.
            total_sum_of_digits += digit
            # Remove the last digit from the number using floor division.
            current_number //= 10
            
    # Print the final sum after the loops are complete.
    print(total_sum_of_digits)

# Call the function with the list.
list1 = [234, 344, 53, 97, -586]
sum_digits(list1)




