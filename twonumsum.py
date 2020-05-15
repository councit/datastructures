# Two Number Sum

'''
Given an array of different numbers and a target value...
return the first two numbers that sum to the target value
if there are no solutions return an exmpty array
'''



# #Solution 1 Brute Force: Two for loops
# # Spact = O(1), Time = O(n^2)

# def two_num_sum(array, target_sum):
# 	for i in array:
# 		search_num = target_sum - i
# 		for j in array:
# 			if search_num == j:
# 				return [i, j]

# 	return []


#Solution 2: Hash Tables
#Space: O(N) Time: O(N)

# def two_num_sum(array, target_sum):
# 	observed_numbers = {}

# 	for number in array:
# 		search_value = target_sum - number
# 		if search_value in observed_numbers:
# 			return [number, search_value]
# 		else:
# 			observed_numbers[number] = True
# 	return []


#Solution 3: Moving Pointers
#Space: O(N*Log(N)) Time: O(1)

def two_num_sum(array, target_sum):
	array.sort()
	left = 0
	right = len(array) - 1 # init pointer locations

	while left < right:
		current_sum = array[left] + array[right]

		if current_sum == target_sum:
			return [array[left], array[right]]
		elif current_sum < target_sum:
			left += 1
		elif current_sum > target_sum:
			right -= 1
	return []






# Test
arr1 = [1,2,3,4,5,6,7,8,9,10]
target1 = 13
#result = [3,10]


arr2 = [-3,4,6,0,9]
target2 = 1
#result = [-3,2]

arr3 = [1,2,3]
target3 = 9
#result = []

print(two_num_sum(arr1, target1))
print(two_num_sum(arr2, target2))
print(two_num_sum(arr3, target3))