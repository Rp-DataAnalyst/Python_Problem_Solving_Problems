

# for i in range(len(list1)):
# 	for j in range(len(list1[i])):
# 		print(list1[i][j],end=' ')
# 	print()



# for row in list1:
#     for val in row:
#         print(val, end=" ")
#     print()

# to get all elements from first row:
# list1 = [[1,2,3],[4,5,6],[7,8,9]]   
# for i in range(len(list1)):
# 		for j in range(len(list1[i])):
# 				if i == 0:
# 					print(list1[i][j], end = " ")
# 				else:
# 					print(' ', end = " ")
				
# 		print()

# to get all elements from 2 row:

# list1 = [[1,2,3],[4,5,6],[7,8,9]]   
# for i in range(len(list1)):
# 		for j in range(len(list1[i])):
# 				if i == 1:
# 					print(list1[i][j], end = " ")
# 				else:
# 					print(' ', end = " ")
				
# 		print()

# to get all elements from 3 row:

# list1 = [[1,2,3],[4,5,6],[7,8,9]]   
# for i in range(len(list1)):
# 		for j in range(len(list1[i])):
# 				if i == 2:
# 					print(list1[i][j], end = " ")
# 				else:
# 					print(' ', end = " ")
				
# 		print()
# to get all elements from the first column:
# list1 = [[1,2,3],[4,5,6],[7,8,9]]   
# for i in range(len(list1)):
# 		for j in range(len(list1[i])):
# 				if j == 0:
# 					print(list1[i][j], end = " ")
# 				else:
# 					print(' ', end = " ")
				
# 		print()

# to get all elements from the second column:

# list1 = [[1,2,3],[4,5,6],[7,8,9]]   
# for i in range(len(list1)):
# 		for j in range(len(list1[i])):
# 				if j == 1:
# 					print(list1[i][j], end = " ")
# 				else:
# 					print(' ', end = " ")
				
# 		print()	



#to get all elements from column3:
# list1 = [[1,2,3],[4,5,6],[7,8,9]]   
# for i in range(len(list1)):
# 		for j in range(len(list1[i])):
# 				if j == 2:
# 					print(list1[i][j], end = " ")
# 				else:
# 					print(' ', end = " ")
				
# 		print()

# to get all principal(main) diagonal elements from matrix:

# list1 = [[1,2,3],[4,5,6],[7,8,9]]   
# for i in range(len(list1)):
# 		for j in range(len(list1[i])):
# 				if i == j:
# 					print(list1[i][j], end = " ")
# 				else:
# 					print(' ', end = " ")
				
# 		print()

# to get all Secondary(anty) diagonal elements from matrix:


# list1 = [[1,2,3],[4,5,6],[7,8,9]]   
# for i in range(len(list1)):
# 		for j in range(len(list1[i])):
# 				if i+j == 2: #if i+j == len(list1)-1
# 					print(list1[i][j], end = " ")
# 				else:
# 					print(' ', end = " ")
				
# 		print()

# to get both principal/main elements from matrix:

# list1 = [[1,2,3],[4,5,6],[7,8,9]]   
# for i in range(len(list1)):
# 		for j in range(len(list1[i])):
# 				if i+j == 2 or  i == j :   #if i+j == len(list1)-1
# 					print(list1[i][j], end = " ")
# 				else:
# 					print(' ', end = " ")
				
# 		print()


#Sum of all diagonal elements of a matrix: common element adds single time

# sum=0
# list1 = [[1,2,3],[4,5,6],[7,8,9]]   
# for i in range(len(list1)):
# 		for j in range(len(list1[i])):
# 				if i+j == 2 or  i == j :   #if i+j == len(list1)-1
# 					sum += list1[i][j]
					
# 					print(list1[i][j], end = " ")
# 				else:
# 					print(' ', end = " ")
				
# 		print()
# 		print(sum)

#Sum of all diagonal elements of a matrix: common element adds 2 times:


# sum=0
# list1 = [[1,2,3],[4,5,6],[7,8,9]]   
# for i in range(len(list1)):
# 		for j in range(len(list1[i])):
# 				if i == j :   #if i+j == len(list1)-1
# 					sum += list1[i][j]
# 				if i+j == 2 :
# 					sum += list1[i][j]
# 		print(sum)


#Check if the given matrix is identity matrix or not 




list1 = [[1,0,0],[0,1,0],[0,0,1]]   
def is_identity_matrix(list1):
	for i in range(len(list1)):
			for j in range(len(list1[i])):
				if i == j and list1[i][j] != 1:
					return False
				elif i != j and list1[i][j] !=0 :
					return False
			return True 
	 
 
print(is_identity_matrix(list1))
		 










	


