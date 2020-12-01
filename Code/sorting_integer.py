from sorting_iterative import insertion_sort

#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n + K (max of numbers)) we loop through input array and 
    then the array of size max(numbers)
    TODO: Memory usage: O(k) as we create a new array of size O(max of numbers)"""
    max_value = max(numbers)
    counts = [0] * (max_value + 1)
    for item in numbers:
        counts[item] += 1

    # Overwrite counts to hold the next index an item with
    # a given value goes. So, counts[4] will now store the index
    # where the next 4 goes, not the number of 4's our
    # list has.
    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count

    # Output list to be filled in
    sorted_list = [None] * len(numbers)

    # Run through the input list
    for item in numbers:

        # Place the item in the sorted list
        sorted_list[ counts[item] ] = item

        # And, make sure the next item we see with the same value
        # goes after the one we just placed
        counts[item] += 1

    return sorted_list



def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? 2*O(num_buckets) + O(n) + insertion_sort. Because we 
    loop num_buckets times to initalize an array
    loop n times to place number in the right bucket loop num_buckets times
    TODO: Memory usage: ??? O(num_buckets)"""
    arr = []
    for i in range(num_buckets): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for j in numbers: 
        index_b = int(num_buckets * j)
        arr[index_b].append(j) 
      
    # Sort individual buckets  
    for i in range(num_buckets): 
        arr[i] = insertion_sort(arr[i]) 
          
    # concatenate the result 
    k = 0
    for i in range(num_buckets): 
        for j in range(len(arr[i])): 
            numbers[k] = arr[i][j] 
            k += 1
    return numbers


print(counting_sort([3, 2, 1, 24, 5, 2]))
print(bucket_sort([0.25, 0.36, 0.58, 0.41, 0.29]))