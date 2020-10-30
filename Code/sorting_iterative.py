#!python
def swap(i, j, items):
    items[i], items[j] = items[j], items[i]

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Time Complexity O(n) since we iterate over the array until we find two unsorted elements
    Space Complexity O(1)
    """
    # TODO: Check that all adjacent items are in order, return early if so
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Worst Case Time Complexity O(n*n)-> comparing two adjecent elements for as many elements there are in the list
    Best Case O(n) if items is already sorted
    Average Case O(n*n)

    Space Complexity O(1)
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    total_swaps = 0
    for _ in range(len(items)):
        for j in range(len(items)-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                total_swaps += 1
        if total_swaps == 0:
            return items # Handling Best Case i.e. sorted array O(n)
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Time Complexity O(n*n) left sublist is always sorted. We find the new smallest element in 
    the unsorted list and do this operation n number of times. This is the worst performing algorithm.
    Space Complexity O(1)
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    for i in range(len(items)-1):
        smallest = i
        for j in range(i+1, len(items)):
            if items[smallest] > items[j]:
                smallest = j
        swap(smallest, i, items)
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?
    Worst Case Time Complexity O(n*n) We keep swaping the smallest element as long as we are in bound.
    Best Case --> O(n) because inner while loop is never triggred.
    Average Case O(n*n)

    Space Complexity O(1)
    """
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            swap(j, j-1, items)
            j -= 1
    return items