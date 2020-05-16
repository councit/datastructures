'''
Finding subsequence given two arrays
Plan: Use pointers to move through sub array and main array. Once num found move on to next sub array num
if you reach the end of the subarray then return True
'''

def validate_sequence(array, sequence):
	arr_pointer = 0
	seq_pointer = 0

	while arr_pointer < len(array) and seq_pointer < len(sequence):
		if array[arr_pointer] == sequence[seq_pointer]:
			seq_pointer += 1
		arr_pointer += 1
	return seq_pointer == len(sequence)


# Test
test_arr = [0,1,2,3,4,5]
test_seq = [2,3,4]

print(validate_sequence(test_arr,test_seq))