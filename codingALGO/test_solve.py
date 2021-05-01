import pytest
from solve import count_sum_lists

def test1():
	A = [1, 2, 8]
	k = 1000
	B = 2	
	res = count_sum_lists(A, k, B)
	assert res == 3

def test2():
	A = [5, 17, 10000, 11]
	k = 1000
	B = 4
	res = count_sum_lists(A, k, B)
	assert res == 0