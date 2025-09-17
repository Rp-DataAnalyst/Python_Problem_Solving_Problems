#Sorting
#Sorting algorithms: Bubble Sorting, Merge sort, Quick Sorting
# list1= [10,-3,700,45,23,100,-300]
# for j in range(0,6): # outer loop for iterating all items in list
#       flag = False
#       for i in range(0,len(list1)-1-j): # inner loop for moving max item to last index
#             if list1[i] > list1[i+1]:
#                   flag = True
#                   list1[i], list1[i+1] = list1[i+1], list1[i]
#       if flag == False:
#             break 
# print(list1)

#Searching:
# Searching Algorithms Linear Search, Binary Search:
#Linerar search will work on any list , Binary search will work only on sorted list.
# list1 = [23,32,53,23,12,33]
# search_element = 33
# flag = True 
# for ind in range(0,len(list1)-1):
#       if list1[ind] == search_element:
#             print(ind)
#             flag = False 
#             break 
# if flag == True:
#       print('Not Found')

# def linear_search(list1, search_elem):
#       for i in range(len(list1)):
#             if list1[i] == search_elem:
#                   return i
#       return False 

#Can you write bobble sort for descending order:
def bobble_sort(list1):
      for j in range(0,len(list1)):
            for i in range(len(list1)-1-j):
                  if list1[i] < list1[i+1]:
                        list1[i] , list1[i+1] = list1[i+1], list1[i]

      print(list1)


list1= [12,3,4,56,55,43]
bobble_sort(list1)
# the elements in a string sorted based on their order in the dictionary.

bobble_sort(['ram','shyam','vasu','venu'])
#Use bobble sort to sort things based on their length:
students= ['ram','shyam', 'venu', 'santhu', 'rohith']
def sort_strings_based_on_lengths(str1):
      for j in range(len(str1)-1):
            for i in range( len(str1)-1-j):
                  if len(str1[i][0])> len(str1[i+1][0]):
                        str1[i][0], str1[i+1][0]
      print(str1)
sort_strings_based_on_lengths(students)

def nested_list(list1):
      for j in range(len(list1)-1):
            for i in range(len(list1)-1-j):
                  if list1[i][0] < list1[i+1][0]:
                        list1[i],list1[i+1]  = list1[i+1], list1[i]
      print(list1)
list1 =  [[12, 5], [3, 8], [4, 2], [56, 1], [55, 9], [43, 6]]
nested_list(list1)











               