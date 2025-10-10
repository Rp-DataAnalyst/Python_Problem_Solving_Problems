#Alphabet "D":

# n = 7

# for i in range(n):
#  for j in range(n):
#   if j == 0 or i == 0   or i == n-1   or j == n-1:
#    if ( i == 0 and j == n-1) or (i == n-1 and j == n-1):
#     print(" ", end=" ")
#    else:
#     print("*", end=" ")
#   else:
#    print(" ", end=" ")

#  print()   



#Alphabet "G" :


# n = 7
# for i in range(n):
#  for j in range(n):
#   if i == 0 or j == 0 or i == n-1 or (j == n-1 and i >= n//2) or (i == n//2 and j >= n//2 ):
#    print('*', end=" ")
#   else:
#    print(" ", end=" ")
#  print()


#Alphabet "J":


# n = 7
# for i in range(n):
#  for j in range(n):
#   if i == 0 or ( j == n//2) or (i == n-1 and j <= n//2) or (j == 0 and i >= n//2)  :  
#    print('*', end=" ")
#   else:
#    print(" ", end=" ")
#  print()  


#Alphabet " K ": we can print K pattern using slope equation method and v ^ method we are using 2 method:

# n = 4
# for i in range(n):
#  for j in range(n):
#   if j == 0 or i+j == n-1 : 
#    print('*', end=" ")
#   else:
#    print(" ", end=" ")
#  print()

# for i in range(1,n):
#   for j in range(n):
#    if j == 0 or i == j :
#     print("*", end= " ")
#    else:
#     print(" ", end= " ")
#   print()


#Alphabet " Q ":


# n = 7
# for i in range(n):
#  for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1 or (i == j and j >= n//2 ) :
#           print('*', end=" ")
#         else:
#           print(" ", end=" ")
#  print()

# for i in range (n+1):
#    if i == n :
#       print("*", end= " ")
#    else:
#       print(" ", end= " ")


#Alphabet " R ":



# n = 5
# for i in range(n):
#    for j in range(n):
#       if i == 0 or j == 0 or i == n//2 or j == n-1 :
#          if (i == 0 and j == n-1) or (i == n//2 and j == n-1):
#             print( " ", end=" ")
#          else:

#           print ( "*", end=" ")
#       else:
#          print(" ", end=" ")

#    print()


#Alphabet " S ":

# n = 7
# for i in range(n):
#  for j in range(n):
#   if i == 0 or i == n-1 or i == n//2 or (j == 0 and i <= n//2) or (j == n-1 and i >= n//2):
#    if (i == n//2 and  j == 0) or (i == n//2 and j == n-1) or ( i == 0 and j == 0) or (i == n-1 and j == n-1 ):
#     print(" ", end=" ")
#    else:

#     print("*", end= " ")
#   else:
#    print( " ", end= " ")

#  print()


#Alphabet " T ":


# n = 5
# for i in range(n):
#  for j in range(n):
#   if i == 0 or    j == n//2 :  
#    print("*", end=" ")
#   else:
#    print(" ", end= " ")
#  print()


#Alphabet " U ":


# n = 5
# for i in range(n):
#  for j in range(n):
#   if i == 0 or    j == n//2 :  
#    print("*", end=" ")
#   else:
#    print(" ", end= " ")
#  print()


#Alphabet " U ":


# n = 5
# for i in range(n):
#  for j in range(n):
#   if i == n-1 or j == 0 or j == n-1:  
#    if (i == n-1 and j == 0) or (i == n-1 and j == n-1):
#     print( " ", end= " ")
#    else:
#     print("*", end=" ")
#   else:
#    print(" ", end= " ")
#  print()


#Alphabet " V ":

# n = 7
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
#     if i == n//2:   # stop at middle row
#         break


#Alphabet " W ":


# n = 5

# for i in range(n):
#  for j in range(n):
#   if j == 0 or j == n-1 or (i+j == n-1 and i >= n//2) or (i == j and i >= n//2 ):
#    print("*", end=" ")
#   else:
#    print(" ", end=" ")
#  print()
    












#Alphabet " X ":

# n = 5
# for i in range(n):
#  for j in range(n):
#   if i == j or i+j == n-1 :  
#    print("*", end=" ")
#   else:
#    print(" ", end= " ")
#  print()



#Alphabet " Y ":


# n = 5

# for i in range(n):
#  for j in range(n):
#   if  (i == j and i <= n//2) or (i+j == n-1 and i <= n//2) or (i >= n//2 and j == n//2):
#    print("*", end=" ")
#   else:
#    print(" ", end=" ")
#  print()  


#Alphabet " Z ":


# n = 5

# for i in range(n):
#  for j in range(n):
#   if i == 0 or i == n-1 or i+j == n-1:
#    print('*', end=" ")
#   else:
#    print(" ", end=" ")
#  print()


#Up arrow :
n = 7   # height of the arrow head (odd number)

# Arrow head (hollow triangle, bottom row filled)
for i in range(n//2 + 1):
    for j in range(n):
        if i + j == n//2 or j - i == n//2 or i == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Arrow shaft
for i in range(n//2):
    for j in range(n):
        if j == n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

