def swap(i, j, items):
    items[i], items[j] = items[j], items[i]

def selection_sort(items):
    for i in range(len(items)-1):
        smallest = i
        for j in range(i+1, len(items)):
            if items[smallest] > items[j]:
                smallest = j
        swap(smallest, i, items)
        print(items)
    return items

selection_sort([23,4, 1, 3, 6, -4, 0])