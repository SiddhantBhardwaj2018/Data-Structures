
def recursive_bubbleSort(lst):
    '''
    This is recursive implementation of bubble sort.
    '''
    for i,num in enumerate(lst):
        try:
            if lst[i + 1] < num:
                lst[i] = lst[i + 1]
                lst[i + 1] = num
                recursive_bubbleSort(lst)
        except IndexError:
            pass
    return lst
    
print(recursive_bubbleSort([5,2,1,4,6,3]))