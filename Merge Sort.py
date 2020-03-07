def merge_sort(lst):
    '''
    '''
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        
        left_pointer = right_pointer = lst_pointer = 0
        
        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer] < right[right_pointer]:
                lst[lst_pointer] = left[left_pointer]
                left_pointer += 1
                lst_pointer += 1
            else:
                lst[lst_pointer] = right[right_pointer]
                right_pointer += 1
                lst_pointer += 1
        
        while left_pointer < len(left):
            lst[lst_pointer] = left[left_pointer]
            left_pointer += 1
            lst_pointer += 1
            
        while right_pointer < len(right):
            lst[lst_pointer] = right[right_pointer]
            right_pointer += 1
            lst_pointer += 1
            
        return lst
    else:
        return lst

merge_sort([5,2,4,6,1,3])