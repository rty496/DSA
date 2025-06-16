from collections import Counter

def frequency_sort(nums):
    count = Counter(nums)
    return sorted(nums, key=lambda x: (count[x], -x))
