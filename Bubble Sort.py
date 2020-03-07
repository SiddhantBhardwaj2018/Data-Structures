
def bubbleSort(lst):
    '''
    This takes time of O(n^2)
    '''
    n = len(lst)
    for i in range(1,n):
        for j in range(0, n-1):
            key = lst[j + 1]
            if lst[j] > lst[j + 1]:
                lst[j + 1] = lst[j]
                lst[j] = key
    return lst
    
print(bubbleSort([5,2,1,4,6,3]))
