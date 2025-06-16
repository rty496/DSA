def sort_array(nums):
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left_part = sort_array(nums[:middle])
    right_part = sort_array(nums[middle:])
    return merge(left_part, right_part)

def merge(left_part, right_part):
    result = []
    i = j = 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j += 1
    result.extend(left_part[i:])
    result.extend(right_part[j:])
    return result
