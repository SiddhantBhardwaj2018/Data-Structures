
'''
Given an array of sorted integers. We need to find the closest value to the 
given number.
Array may contain duplicate values and negative numbers.
'''

def find_closest_num(lst,target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None
    #Edge cases for empty list
    if len(A) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    while low <= high:
        mid = (low + high) // 2
        if mid + 1 < len(lst):
            min_diff_right = abs(lst[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(lst[mid - 1] - target)
        if min_diff_left < min_diff:
            min_diff =  min_diff_left
            closest_num = lst[mid - 1]
            
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num =  lst[num + 1]
        if lst[mid] < target:
            low = mid + 1
        elif lst[mid] > target:
            high = mid  - 1
        else:
            return lst[mid]
    return closest_num