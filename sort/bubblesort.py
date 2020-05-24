# def bubble_sort(array):
# 	isSorted = False # setting bool to check for sorted first, then toggle if needed sort

# 	while not isSorted:
# 		isSorted = True

# 		for i in range(len(array) - 1):
# 			if array[i] > array[i + 1]:
# 				swap(i, i + 1, array)
# 				isSorted = False
# 	return array

# def swap(i, j, array):
# 	array[i], array[j] = array[j], array[i]

# array = [8, 5, 2, 9, 5, 6, 3]
# print(bubble_sort(array))

def bubble_sort(array):
	is_sorted = False
	count = 0

	while not is_sorted:
		is_sorted = True

		for i in range(len(array) - 1 - count):
			if array[i] > array[i + 1]:
				is_sorted = False
				swap(i, i + 1, array)
				count += 1
	return array

def swap(i , j, array):
	array[i], array[j] = array[j], array[i]

array = [8, 5, 2, 9, 5, 6, 3]
print(bubble_sort(array))