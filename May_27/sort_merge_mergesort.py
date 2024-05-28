def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])
    
    return sorted_list

# Lists to be merged and sorted
l1 = [2, 5, 7, 9]
l2 = [1, 3, 6, 7, 10, 13]

# Merging the two lists
merged_list = l1 + l2

# Sorting the merged list using merge sort
sorted_list = merge_sort(merged_list)

print(sorted_list)
