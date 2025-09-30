#Count the number of swaps performed by bubble sort while sorting an array.

def count_swaps_bubble_sort(arr):
	count = 0
	for i in range(len(arr)):
		for j in range(len(arr)-1-i):
			if arr[j] > arr[j+1]:
				arr[j] , arr[j+1] = arr[j+1] , arr[j]
				count+=1
	print(count)


list1 = [12,23,4,5,66,23,98,33,23]
count_swaps_bubble_sort(list1)
 
 # Time complexity = O(n*n) quadratic time complexity.
 # Space complexity =  O(1)



#2 Apply binary search in only first half of the list. (Search only in first half)
def binary_search(list1):
		list1.sort()
					
		low = 0 
		high = (len(list1)//2) - 1
		select_element = 4
		while low <= high:
						mid = (low + high)//2
						if list1[mid] == select_element:
							return mid
						elif list1[mid] < select_element:
							low = mid+1
						else:
							high = mid-1
		return -1


list1 = [12,23,4,5,66,23,98,33,23]

print(binary_search(list1))

#T.C = O(n log n)
#S.C = O(1)




	
	
    		