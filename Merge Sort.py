
def mergeSort(lst):
    '''
    This takes O(n log n) time.
    '''
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        
        mergeSort(left)
        mergeSort(right)
        
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
                k += 1
            else:
                lst[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[j] = right[j]
            j += 1
            k += 1
    else:
        return lst
        
        
