#!python
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

def merge(items1, items2):
	"""Merge given lists of items, each assumed to already be in sorted order,
	and return a new list containing all items in sorted order.
	TODO: Running time: ??? O(n)
	TODO: Memory usage: ??? O(n)"""
	sorted_array = []
	while len(items2) > 0 or len(items1) > 0: # O(n)
		smallest = min(items1 + items2) # O(n)
		sorted_array.append(smallest)
		if smallest in items2:
			items2.remove(smallest)  # O(n)
		else:
			items1.remove(smallest) # O(n)
	return sorted_array


def split_sort_merge(items):
	"""Sort given items by splitting list into two approximately equal halves,
	sorting each with an iterative sorting algorithm, and merging results into
	a list in sorted order.
	TODO: Running time: ??? O(n^2/ 2) each time we sort and items is divided into two
	TODO: Memory usage: ???2*O(n) since we make a copy for items1 and items2"""
	mid = items // 2
	first_half, second_half = items[:mid], items[mid: ]
	first_half_sorted, second_half_sorted = sorted(first_half), sorted(second_half)
	return merge(first_half_sorted, second_half_sorted)


def merge_sort(items):
	"""Sort given items by splitting list into two approximately equal halves,
	sorting each recursively, and merging results into a list in sorted order.
	TODO: Running time: ??? O(n log(n))
	TODO: Memory usage: ??? O(n(log (n)))"""
	if len(items) > 1:
		middle = len(items) // 2
		left, right = items[:middle], items[middle:]
		merge_sort(left)
		merge_sort(right)
		items[:] = merge(left, right)
	
	return items


def partition(items, low, high):
	"""Return index `p` after in-place partitioning given items in range
	`[low...high]` by choosing a pivot (TODO: document your method here) from
	that range, moving pivot into index `p`, items less than pivot into range
	`[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
	TODO: Running time: ??? O(n)
	TODO: Memory usage: ??? O(1)
	# TODO: Choose a pivot any way and document your method in docstring above
	# TODO: Loop through all items in range [low...high]
	# TODO: Move items less than pivot into front of range [low...p-1]
	# TODO: Move items greater than pivot into back of range [p+1...high]
	# TODO: Move pivot item into final position [p] and return index p

	"""
	divider = low #keeps track of the pivot index used for comparision
	pivot = high #default pivot index
	for i in range(low, high):
	# Move items less than pivot into front of range [low...p-1]
	# Move items greater than pivot into back of range [p+1...high]
		if items[i] < items[pivot]: #this does the work
			items[i], items[divider] = items[divider], items[i] # by moving the items less than
			divider += 1 # and leaving items greater where they are
	# Move pivot item into final position [p] and return index p
	items[pivot], items[divider] = items[divider], items[pivot]
	return divider



def quick_sort(items, low=None, high=None):
	"""Sort given items in place by partitioning items in range `[low...high]`
	around a pivot item and recursively sorting each remaining sublist range.
        Best Case: O(n) - The pivot always picks the correct element.
        Average Case: O(n * log n) We amoratize it not always picking the middle value to pivot from.
        Worst Case: O(N^2) when we always pick the lowest/highest element to pivot on
    	Memory usage: O(log n) We do not allocate more memory since we do everything in place, but the call stack takes memory..
	# TODO: Check if high and low range bounds have default values (not given)
	# TODO: Check if list or range is so small it's already sorted (base case)
	# TODO: Partition items in-place around a pivot and get index of pivot
	# TODO: Sort each sublist range by recursively calling quick sort

		"""
	if low is None and high is None:
		low = 0
		high = len(items) - 1

	if low < high:
		# partition the items
		p = partition(items, low, high)
		# sort both half of the partition recursively
		quick_sort(items, low, p-1)
		quick_sort(items, p+1, high)
	
	return items


print(quick_sort([3, 2, 1, 24, 5, 2]))
print(merge_sort([3, 2, 1, 24, 5, 2]))
