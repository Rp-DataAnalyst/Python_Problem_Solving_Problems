#Reverse elements in list1:
#Method:1
list1=[23,55,64,-54]
new_list= list1.reverse()
print(list1)
#Method:2
list1=[23,55,64,-54]
reversed_list=list1[::-1]
print(reversed_list)
#Method:3
def reverse(input_list):
      reversed_list=[]
      for i in input_list:
            reversed_list.insert(0,i)
      return reversed_list

list1=[23,55,64,-54]
print(reverse(list1))
#Method:4
list1=[23,55,64,-54]
new_list=[]
for i in list1:
      new_list.append(i)

print(new_list)
#efficient way
list1=[23,55,64,-54]
low = 0
high= len(list1)-1
while low<high:
      list1[low],list1[high] = list1[high], list1[low]
      low+=1
      high-=1
print(list1)
#reversing half of a list items:
list1=[23,55,64,-54]
low=0
high=(len(list1)-1)//2
while low<high:
      list1[low],list1[high] = list1[high],list1[low]

      low+=1
      high-=1
print(list1)




