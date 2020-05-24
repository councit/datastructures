'''
Given an array return a len 3 list if the sum == target value
'''

def threeNumberSum(array, targetSum):
	array.sort()
	trip_arr = []

	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			currentSum = array[i] + array[left] + array[right]
			if currentSum == targetSum:
				trip_arr.append((array[i], array[left], array[right]))
				left += 1
				right -= 1
			elif currentSum < targetSum:
				left += 1
			elif currentSum > targetSum:
				right -= 1
	return trip_arr







#Test
arr = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0

print(threeNumberSum(arr, target))