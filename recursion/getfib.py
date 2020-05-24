# # O(n) S/T
# def getNthFib(n):
# 	F0 = 0
# 	F1 = 1
# 	retArr = [0,1]

# 	for num in range(2, int(n) + 1):
# 		FNext = F0 + F1
# 		retArr.append(FNext)
# 		F0 = retArr[-2]
# 		F1 = retArr[-1]
# 	print(retArr)

# 	return retArr[-1]

# print(getNthFib('5'))

# def getFib(n):
# 	if n == 2:
# 		return 1
# 	elif n == 1:
# 		return 0 
# 	else:
# 		print(n)
# 		return getFib(n - 1) + getFib(n - 2)
		


# print(getFib(10))

# def getNthFib(n, memoize={1: 0, 2: 1}):
# 	if n in memoize:
# 		return memoize[n]
# 	else:
# 		memoize[n] = getNthFib(n - 1, memoize) + getNthFib( n - 2, memoize)
# 		return memoize[n]

# print(getNthFib(10))