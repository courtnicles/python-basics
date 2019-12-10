""""
DATA 200 Fall 2019 Homework 8
Courtney Nguyen
16NOV19
hw8-3.py
"""

## pass in list and recursive function, low and high index
def quick_sort(A):
	quick_sort2(A, 0, len(A)-1)

def quick_sort2(A, low, hi):
    if low < hi:
        ## partition function call
        p = partition(A, low, hi)
        ## left of pivot
        quick_sort2(A, low, p - 1)
        ## right of pivot
        quick_sort2(A, p + 1, hi)

## mid index and compare
def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid
	return hi

def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
    ## swapping out values
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low

## if item is less than pivot value, swap with border value
	for i in range(low, hi+1):
		if A[i] < pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]
	return (border)

A = [0, 455, 276, 98, 360, 254, 166, 429, 53, 280, 344, 449, 496, 288, 329]
print(A)
quick_sort(A)
print(A)

B = [1000, 999, 345, 928, 60, 24, 16, 42, 533, 180, 374, 439, 96, 188, 32]
print(B)
quick_sort(B)
print(B)