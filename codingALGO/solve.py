"""
Python 3.8
Problem Description:
--------------------
Given a array of integers A of size N and an integer B.
Return number of non-empty subsequences of A of size B having sum <= 1000.
---------------------
Notes
-----
NB1 - Scope for optimisation . <sort the array and do little tweak in the BL.>
NB2 - Using the same varibale names mentioned in the problem statement though
it contradicts the pep8 standard
NB3 - Prefer using tabs instead of spaces though it contradicts pep8.
"""


def count_sum_lists(A, k, B):
	"""
	Inputs- A => list of input elements.
			k => limit sum of subset(each subset should be less than or equal to k)
			B => size of subsets
	Output - Integer count of subsets which obeys the limit sum condition
	"""
	n = len(A)
	start = 0 
	end = B
	count = 0
	sum_ = sum(A[start:B]) 
	while True :
		#  .if sum of subset satisfies the condition, increment the counter
		if sum_ <= k:
			count += 1
		#  if the end pointer is in last position
		#  ..reset the start pointer and end pointer
		#  ...if after resetting pointers, end pointer 
		#     points to outside the scope of list , 
		#     we're done traversing the list. End of the loop.
		#  ...calculate the sum of new subset
		#  else
		#  .increment the end pointer
		#  .calculate the sum of new subset
		if end+1 > n:
			start += 1
			end = start+B
			if end > n:
				break
			sum_ = sum(A[start:end])
		else:
			sum_ += (A[end]-A[end-1]) #  removing existing end pointer element from subset
									  #  and adding new end pointer element to subset
			end += 1
	return count


if __name__ == "__main__":
	A = [1,2,8,4]
	k = 1000
	B = 2
	count = count_sum_lists(A, k, B)
	print(count)
