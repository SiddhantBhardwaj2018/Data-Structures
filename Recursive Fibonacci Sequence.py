
def recursive_fibonacci(n):
    #Recursive implementation of fibonacci sequence
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n - 2) + recursive_fibonacci(n - 1)
        
print(recursive_fibonacci(28))