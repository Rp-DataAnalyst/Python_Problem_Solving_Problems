#Binary Search

# list1 = [-3,-300,10,23,45,100,700]
# list1.sort()
# low = 0
# high = len(list1)-1
# search_element = 1200
# flag = True

# while low <= high:
#       mid = (low+high)//2
#       if list1[mid ]== search_element:
#             print(mid, "Number Found")
#             flag = False 
#             break
#       elif list1[mid] > search_element:
#             high = mid - 1

#       else:
#             low = mid +1
# if flag == True :
#       print('Not Found')

# Writing the above program using function:

def find_index_of_element(list1,search_element):
      
      low = 0
      high = len(list1)-1
      flag = True
      while low <= high:
            mid = (low + high)//2
            if list1[mid] == search_element:
                  print((mid),'element found')
                  flag = False
                  break 
            elif list1[mid] > search_element :
                  high = mid - 1
            else :
                  low = mid +1
      if flag == True :
            print('Not Found')
list1 =  [-300,-3,10,23,45,100,700]
find_index_of_element(list1,100)
       



