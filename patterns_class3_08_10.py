#Pytamid Pattern:


# n = 7
# mid = n//2
# for i in range(n):
#  for sp in range( n - i - 1):  #for no of spaces:
#   print(" ", end="")
  
  
#  for j in range(n):
#   if   i >=j:
#    print("*", end=" ")
#   else:
#    print(" ", end=" ")
#  print()


# print()
# print()
# print()

# Reverse Pyramid:

# n = 7
# mid = n//2
# for i in range(n):
#  for sp in range( i):  #for no of spaces:
#   print(" ", end="")
  
  
#  for j in range(n):
#   if   i+j <= n-1:
#    print("*", end=" ")
#   else:
#    print(" ", end=" ")
#  print()



#Diamond Pattern:


# n = 7
# mid = n//2
# for i in range(n):
# 	for sp in range(n-i-1):
# 		print(" ", end="")
				
# 	for j in range(n):
# 		if i >= j:
# 			print("*", end= " ")
# 		else:
# 			print(" ", end=" ")
# 	print()
# for i in range(1,n):
#  for sp in range( i):  #for no of spaces:
#   print(" ", end="")
  
  
#  for j in range(n):
#   if   i+j <= n-1:
#    print("*", end=" ")
#   else:
#    print(" ", end=" ")
#  print()
		

#Parallelogram  Pattern:

# n = 7
# for i in range(n):
#      for sp in range(n-i-1):
#           print(" ", end="")
#      for j in range(n):
#           print("*", end=" ")
#      print()
          
#Rhombus Pattern:


# n = 7
# for i in range(n):
#      for sp in range(i):
#           print(" ", end="")
#      for j in range(n):
#           print("*", end=" ")
#      print()

#Number Pyramid Pattern :


# n = 4
# mid = n//2
# curr = 1
# for i in range(n):
# 	for sp in range(n-i-1):
# 		print(" ", end="")

# 	for j in range(n):
# 		if i >= j :
# 			print(curr, end=" ")
# 			curr+=1
# 		else:
# 			print(" ", end=" ")
# 	print()


#Number Increasing Triangle:

# n = 4
# mid = n//2
# curr = 1
# for i in range(n):
# 	for sp in range(n-i-1):
# 		print(" ", end="")

# 	for j in range(n):
# 		if i >= j :
# 			print(curr, end=" ")
			
# 		else:
# 			print(" ", end=" ")
# 	print()
# 	curr+=1


#Number Decreasing Order:

# n = 4
# mid = n//2

# for i in range(n):
# 	curr = 1
# 	for j in range(n):
# 		if i+j <= n-1 :
# 			print(curr, end=" ")
# 			curr+=1
			
# 		else:
# 			print(" ", end=" ")
	
		
# 	print()

#Alphabet zero one pattern:

# n = 5
# mid = n//2
# curr = 0

# for i in range(n):
# 	for j in range(i+1):
# 		if (i + j)%2 == 0 :
			
# 				print("1", end=" ")
# 		else:
# 				print("0", end=" ")
# 	print()


#Hollow Trianlge Pattern:
# n = 5   # height of the triangle

# for i in range(n):
#     # spaces before stars
#     for sp in range(n - i - 1):
#         print(" ", end="")

#     # stars and hollow inside
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i or i == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#Butterfly Pattern:

# n = 5

# for i in range(n):
# 	for j in range(n):
# 		if (i >= j and i+j <= n-1) or (i+j >= n-1 and i <= j) :
# 			print("*", end=" ")
# 		else:
# 			print(" ", end=" ")
# 	print()

#Time Saver Pattern:

# n = 5

# for i in range(n):
# 		for j in range(n):
# 				if (j >= i and i+j <= n-1) or (j <=i and i+j >= n-1) :
# 					print("*", end=" ")
# 				else:
# 					print(" ", end=" ")
# 		print()


#Mirror Image  Triangle Pattern:

# n = 7
# mid = n//2
# for i in range(1, n+1):
	
# 	for sp in range( i):  #for no of spaces:
# 		print(" ", end="")
# 	for j in range(i, n+1):
# 		print(j, end=" ")

# 	print()
		
		 
# for i in range(n-1,0,-1):
# 	for sp in range(i):
# 		print(" ", end="")
# 	for j in range(i, n+1):
# 		print(j, end=" ")
# 	print()


# Right Pascal Triangle Pattern:



 
n = 7

# visible = True

for i in range(n):
	
		if i%2 == 0:
			visible = True
		else:
			visible = False

		for j in range(n):
			if ((i >= j)) and (i+j <= n-1):
				if visible == True:
					print("*", end=" ")
					visible = False
				else:
					print(' ', end=" ")
					visible = True
			else:
				print(" ", end=" ")


		print()

		
  
  



        
