#patterns:

 #It will work only in python and JS so we nedd to avoid this and use only for loops for generating patterns.

# for i in range(3):
# 	print("*")
	
# n=5
# for i in range(n):
# 	for j in range(n):
# 		if j == n//2:
# 			print("*",end=" ")
# 		else:
# 			print("$ ", end=" ")
# 	print()



#Right Angled Triangle:


# n=5
# for i in range(n):
#  for j in range(n):
#   if i>= j :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
   
#inverted triangle: 
# n=5
# for i in range(n):
#  for j in range(n):
#   if j>= i :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
 

#NE symbol:

# n= 7
# for i in range(n):
#  for j in range(n):
#   if j>= i or i+j == n-1:
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
 

# print("=============================")
# print()
#SW direction pattern:
# n= 7
# for i in range(n):
#  for j in range(n):
#   if i>= j or i+j == n-1:
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
 
# print()
# print()
# print()
#NW direction pattern:

# n= 7
# for i in range(n):
#  for j in range(n):
#   if i+j <= n-1  or i == j:
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()

#SE direction pattern:

# n= 7
# for i in range(n):
#  for j in range(n):
#   if i+j >= n-1  or i == j:
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()

#Hollow Rectangle:


# n= 5
# for i in range(n):
#  for j in range(n):
#   if i == n-1 or i== 0 or j == 0  or j == n-1 :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()  
 


#Hollow Triangle:
# n= 5
# for i in range(n):
#  for j in range(n):
#   if i == n-1 or j == 0  or i == j :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()


# Hollow Triangle2:

# n= 5
# for i in range(n):
#  for j in range(n):
#   if i == n-1 or j == n-1  or i+j == n-1 :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
 

# Alphabet "A":

# n= 5
# for i in range(n):
#  for j in range(n):
#   if i == 0 or j == n-1  or j == 0 or i == n//2 :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
 

# Alphabet "B":

# n= 5
# for i in range(n):
#  for j in range(n):
#   if i == 0 or j == n-1  or j == 0 or i==n-1 or i == n//2 :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()


#Alphabet: "C" :

# n= 5
# for i in range(n):
#  for j in range(n):
#   if i == 0 or i== n-1  or j == 0  :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()


#Alphabet "E":

# n= 5
# for i in range(n):
#  for j in range(n):
#   if i == 0 or i == n-1 or j == 0 or i == n//2 :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
 


#Alphabet "F"


# n= 5
# for i in range(n):
#  for j in range(n):
#   if i == 0 or j == 0 or i == n//2 :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
 

#Alphabet "H":

# n= 5
# for i in range(n):
#  for j in range(n):
#   if   j == 0 or j==n-1 or i == n//2 :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
 

# Alphabet "I" :

# n= 5
# for i in range(n):
#  for j in range(n):
#   if i == 0 or i== n-1 or j == n//2 :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
 


#Alphabet "L" :

# n= 5
# for i in range(n):
#  for j in range(n):
#   if  j == 0 or i == n-1  :
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()

#Alphabet "M" :


# n= 5
# for i in range(n):
#  for j in range(n):
#   if j == n-1 or j == 0 or (i == j and i <= n//2) or (i+j == n-1 and i <= 2):
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
 

#Alphabet "N":

#Alphabet "N"


# n= 5
# for i in range(n):
#  for j in range(n):
#   if j == 0 or j == n-1 or i == j:
#    print('N', end=" ")
#   else:
#    print(' ', end= " ")
#  print()
 




#Alphabet "O":

# n= 5
# for i in range(n):
#  for j in range(n):
#   if j == n-1 or j == 0 or i == 0 or i == n-1:
#    print('*', end=" ")
#   else:
#    print(' ', end= " ")
#  print()


#Alphabet "P":

n= 5
for i in range(n):
 for j in range(n):
  if i == 0 or j == 0 or i == n//2 or (j == n-1 and i < n//2)   :
    print('*', end=" ")
  else:
   print(' ', end= " ")
 print()


