

# def check_monotonic(array):
# 	if len(array) <= 1:
# 		return True


# 	l_point = array[0]
# 	r_point = array[1]
# 	slope = None
# 	check = True



# 	if l_point == r_point:
# 		slope = 'flat'
		
# 	elif l_point > r_point:
# 		slope = 'decreasing'

# 	else:
# 		slope = 'increasing'

# # 	#check
# # 	return slope #returned increasing
# # print(check_monotonic(arr))
# 	print(l_point, r_point, 'a')
# 	for i in range(len(array) - 1):
# 		l_point = array[i]
# 		r_point = array[i + 1]
# 		print(l_point, r_point)

	
# 		if slope == 'increasing' and not l_point <= r_point:
# 			print(l_point, r_point, check, 'b')
# 			check = False
# 		elif slope == 'decreasing' and not l_point >= r_point:
# 			print(l_point, r_point, check, 'c')
# 			check = False





# 	return check
			
arr = [-1, -5, -10, -1100, -900, -1101, -1102, -9001]
def check_monotonic(array):
	direction = {}

	for i in range(len(array) - 1):
		# print(array[i], direction)

		if array[i + 1] - array[i] == 0:
			direction['flat'] = 1
		elif array[i + 1] - array[i] > 0:
			direction['increasing'] = 1
		elif array[i + 1] - array[i] < 0:
			direction['decreasing'] = 1
	
	if 'increasing' in direction and 'decreasing' in direction:
		return False
	elif len(direction) > 2:
		return False
	else:
		return True


	


print(check_monotonic(arr))




