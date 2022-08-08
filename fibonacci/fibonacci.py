def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def itself(n):
    return_str = 'You typed: '+str(n)
    return return_str