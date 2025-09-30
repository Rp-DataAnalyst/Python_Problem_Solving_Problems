l = [[11, 22, 33],
     [444, 55, 66],
     [77, 88, 99]]
# make all values in the matrix is equal to zero.
# for i in range(len(l)) :
# 	for j in range (len(l)):
# 		l[i][j]=0
# print(l)
# print sum of each row in matrix:
for i in range(len((l))):
	sum = 0
	for j in range(len((l))):
		sum+=l[i][j]
	print(sum)


l2 = [[11, 22, 33],
     [444, 55, 66],
     [77, 88, 99]]

for i in range(len(l2)):
	for j in range(len(l2)):
		if i == j :
			l[i][j] = 0
print(l2)


for i in range(len(l)):
	for j in range(len(l)):
		if i+j ==2:
			l2[i][j] = 0 
print(l2)

 


