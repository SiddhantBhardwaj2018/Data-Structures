
def binary_search_recursive(data,target,low,high):
    '''
    Recursive implementation of binary search algorithm
    '''
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data,target,low,mid - 1)
        else:
            return binary_search_recursive(data,target,mid + 1,high)
            
