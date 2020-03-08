
from random import randint

def quickSort(lst):
    '''
    This is the random pivot implementation of the quicksort algorithm.
    Worst case time complexity of O(n^2).
    '''
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[randint(0,len(lst) - 1)]
        smaller,equal,larger = [],[],[]
        for i in range(len(lst)):
            if lst[i] < pivot:
                smaller.append(lst[i])
            elif lst[i] == pivot:
                equal.append(lst[i])
            else:
                larger.append(lst[i])
    return quickSort(smaller) + equal + quickSort(larger)
    
print(quickSort([5,2,1,4,6,3]))