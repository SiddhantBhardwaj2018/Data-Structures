
def binary_search(lst,target):
    '''
    Implements binary search algorithm in python
    '''
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == lst[mid]:
            return True
        elif target < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False