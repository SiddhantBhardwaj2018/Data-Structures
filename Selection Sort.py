
def selectionSort(lst):
    '''
    This is O(n^2) time complexity algorithm.
    '''
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1,len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j 
        lst[min_idx],lst[i] = lst[i],lst[min_idx]
    return lst
    
print(selectionSort([5,2,1,6,4,3]))