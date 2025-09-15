#list_problems
def find_element(input_list1,input_index):
      if input_index < - len(input_list1) or input_index >= len(input_list1):
            return 'Invalid Entry'
      return input_list1[input_index]

input_list1=[1,2,3,4,5,6,7]
input_index=int(input('enter a index number :'))
print(find_element(input_list1,input_index))
 
def find_num(input_list):
      if len(input_list)==0:
            return 'Empty List'
      max_nun = input_list[0]
      for i in input_list:
            if i > max_nun:
                  max_nun=i
      print(max_nun)
list1=[34,56,47,56,-44]
find_num(list1)
#find_min_num:
def find_num(input_list):
      if len(input_list)==0:
            return 'Empty List'
      min_nun = input_list[0]
      for i in input_list:
            if i < min_nun:
                  min_nun=i
      print(min_nun)
list1=[34,56,47,56,-44]
find_num(list1)
def sum_max_min_element_list(input_list):
      if len(input_list) == 0:
            return 'empty list'
      
      sum_of_elements = 0
      max_element = input_list[0]
      min_element = input_list[0]
      for i in input_list:
            sum_of_elements+=i 
            if i > max_element:
                  max_element = i
            if i < min_element:
                  min_element = i 
      return f"Sum: {sum_of_elements}, Max: {max_element}, Min: {min_element}"
list1= [23,4,54,65,-45]
print(sum_max_min_element_list(list1)) 
