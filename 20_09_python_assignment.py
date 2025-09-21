#Wap to check if each number in an  list contains duplicate digits, returning true for duplicates and false for unique digits.



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


# Sum of all numbers in a matrix:

def sum_of_all_numbers_in_a_matrix(matrix1):
        
    total = 0
    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            total += matrix1[i][j]
    print(total)


matx = [3,4,5,4], [23,45,33,5], [7,68,4,3]
sum_of_all_numbers_in_a_matrix(matx)
                    
        
    


