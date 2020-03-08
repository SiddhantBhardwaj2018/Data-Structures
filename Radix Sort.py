
def counting_sort(lst,exp):
    '''
    '''
    size = len(lst)
    output = [0] *  size
    count = [0] * 10
    for i in range(0,size):
        index = lst[i] // exp
        count[index % 10] += 1
    for i in range(1,10):
        count[i] += count[i - 1]
    i =  size - 1
    while i >= 0:
        index =  lst[i] // exp
        output[count[index % 10] - 1] =  lst[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0,size):
        lst[i] = output[i]
    
    
def radix_sort(lst):
    '''
    '''
    max_number = max(lst)
    exp = 1
    while max_number/exp > 0:
        counting_sort(lst,exp)
        exp *= 10
    return lst
    
print(radix_sort([5,2,1,6,4,3]))        