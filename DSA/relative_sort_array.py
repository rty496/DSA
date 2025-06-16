def relative_sort_array(arr1, arr2):
    count_map = {x: 0 for x in arr2}
    remaining_elements = []
    
    for num in arr1:
        if num in count_map:
            count_map[num] += 1
        else:
            remaining_elements.append(num)
    
    result = []
    for num in arr2:
        result.extend([num] * count_map[num])
    
    return result + sorted(remaining_elements)
