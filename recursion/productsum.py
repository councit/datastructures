arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

def recurse(array, multi = 1):
	currentSum = 0

	for item in array:
		if type(item) == list:
			currentSum += recurse(item, multi + 1)
		else:
			currentSum += item

	return currentSum * multi


print(recurse(arr))