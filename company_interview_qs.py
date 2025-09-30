
# Sum of 2 largest elements among 3:


# a = 11
# b = 11
# c= 11
# if a <= b and a <= c:
#  print(b+c)
# elif b <= c and b <= a:
#  print(a+c)
# else:
#  print(a+b)


# Method:2

# a,b,c = map(int, input().split())
# if a>b and a>c:
#  if b>c: print(a+b)
#  else: print(a+c)
# elif b>c and b>a:
#  if a>c: print(a+b)
#  else: print(b+c)
# else:
#  if a>b: print(c+a)
#  else: print(c+b)

# rotation of a matrix:

m = [[1,2,3],
     [4,5,6],
     [7,8,9]]


# #o/p: [[7,4,1],
#        [8,5,2],
#        [9,6,3]]

for i in range(len(m)):
 for j in range(len(m)-1,-1,-1):
  print(m[j][i], end=" ")
 print()


 integer_1 = int(input('enter a num'))

 float_1 = float('enter a float')

 string1 = input('enter a string')

 a,b,c = map(int,input().split())

 list1 = list(map(int,input().split()))


 row = int(input())

 column = int(input())

 matrix = []
 for i in range(n):
  l=list(map(int, input().split()))
  matrix.append(l)




