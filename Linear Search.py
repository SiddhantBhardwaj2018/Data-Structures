
def linear_search(lst,target):
    '''
    Implementation of Linear Search Algorithm in Python
    '''
    for i in range(len(lst)):
        if lst[i] == target:
            return "Found"
    return "Not There"