#!python
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

def merge(items1, items2):
	"""Merge given lists of items, each assumed to already be in sorted order,
	and return a new list containing all items in sorted order.
	TODO: Running time: ??? Why and under what conditions? O(2n * n)-->O(n^2) where k is the no of items in items2
	TODO: Memory usage: ??? Why and under what conditions?"""
	# TODO: Repeat until one list is empty
	# TODO: Find minimum item in both lists and append it to new list
	# TODO: Append remaining items in non-empty list to new list
	sorted_array = []
	while len(items2) > 0 or len(items1) > 0: # O(n)
		smallest = min(items1 + items2) - # O(n)
		sorted_array.append(smallest)
		if smallest in items2:
			items2.remove(smallest)  # O(n)
		else:
			items1.remove(smallest) # O(n)
	return print(sorted_array)
		



def split_sort_merge(items):
	"""Sort given items by splitting list into two approximately equal halves,
	sorting each with an iterative sorting algorithm, and merging results into
	a list in sorted order.
	TODO: Running time: ??? Why and under what conditions?
	TODO: Memory usage: ??? Why and under what conditions?"""
	# TODO: Split items list into approximately equal halves
	# TODO: Sort each half using any other sorting algorithm
	# TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
	"""Sort given items by splitting list into two approximately equal halves,
	sorting each recursively, and merging results into a list in sorted order.
	TODO: Running time: ??? Why and under what conditions?
	TODO: Memory usage: ??? Why and under what conditions?"""
	# TODO: Check if list is so small it's already sorted (base case)
	# TODO: Split items list into approximately equal halves
	# TODO: Sort each half by recursively calling merge sort
	# TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
	"""Return index `p` after in-place partitioning given items in range
	`[low...high]` by choosing a pivot (TODO: document your method here) from
	that range, moving pivot into index `p`, items less than pivot into range
	`[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
	TODO: Running time: ??? Why and under what conditions?
	TODO: Memory usage: ??? Why and under what conditions?"""
	# TODO: Choose a pivot any way and document your method in docstring above
	# TODO: Loop through all items in range [low...high]
	# TODO: Move items less than pivot into front of range [low...p-1]
	# TODO: Move items greater than pivot into back of range [p+1...high]
	# TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
	"""Sort given items in place by partitioning items in range `[low...high]`
	around a pivot item and recursively sorting each remaining sublist range.
	TODO: Best case running time: ??? Why and under what conditions?
	TODO: Worst case running time: ??? Why and under what conditions?
	TODO: Memory usage: ??? Why and under what conditions?"""
	# TODO: Check if high and low range bounds have default values (not given)
	# TODO: Check if list or range is so small it's already sorted (base case)
	# TODO: Partition items in-place around a pivot and get index of pivot
	# TODO: Sort each sublist range by recursively calling quick sort
	quicksort_helper(items, 0, len(items)-1)
	return items


def quicksort_helper(array, start_id, end_id):
	if start_id >= end_id:
		return
	pivot_id = start_id
	left_id = start_id + 1
	right_id = end_id
	while right_id >= left_id:
		if array[left_id] > array[pivot_id] and array[right_id] < array[pivot_id]:
			swap(left_id, right_id, array)
		if array[left_id] <= array[pivot_id]:
			left_id += 1
		if array[right_id] >= array[pivot_id]:
			right_id -= 1
	swap(pivot_id, right_id, array)
	left_sub_array_smaller = right_id - 1 - start_id < end_id - (right_id + 1)
	if left_sub_array_smaller:
		quicksort_helper(array, start_id, right_id - 1)
		quicksort_helper(array, right_id + 1, end_id)
	else:
		quicksort_helper(array, right_id + 1, end_id)
		quicksort_helper(array, start_id, right_id - 1)

merge([1, 3, 5], [2, 4, 6])