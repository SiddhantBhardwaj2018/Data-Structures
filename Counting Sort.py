
def counting_Sort(lst):
    '''
    This is a non-comparison sorting algorithm.
    Takes linear time complexity.
    '''
    max_num = max(lst)
    new_list = [0] * (max_num + 1)
    result_lst = []
    for i in lst:
        new_list[i] += 1
    for i in range(len(new_list)):
        if new_list[i] != 0:
            result_lst += [i] * new_list[i]
    return result_lst
    
print(counting_Sort([5,2,1,4,6,3]))