
def binary_search(sequence, item):
    begin_index =0
    end_index= len(sequence)-1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2

        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        
        elif item < midpoint_value:
            end_index = midpoint -1 

        else:
            begin_index= midpoint +1

    return None




def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


print(quick_sort([5,64,3,4,9,8,7,2,11,34,66,77,89]))

quick_sort_result = quick_sort([5,64,3,4,9,8,7,2,11,34,66,77,89])

sequence_a=quick_sort_result
item_a =77

print(binary_search(sequence_a, item_a))
