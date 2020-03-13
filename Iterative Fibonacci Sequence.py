
def iterative_fibonacci(n):
    #Iterative implementation of Fibonacci sequence at position n. Returns nth value
    a,b = 0,1
    for i in range(n):
        a,b = b,a + b
    return a