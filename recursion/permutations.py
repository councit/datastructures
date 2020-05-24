def sum_list(array):
	#base case
	if len(array) == 1:
		return array[0]
	else:
		return array[0] + sum_list(array[1:])
		

array = [1,2,3,4,5]

print(sum_list(array))


