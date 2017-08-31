#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    if n == 0:
         return 0
    elif n == 1:
        return 1
    else:
        term = 0
        first = 0
        second = 1
        while term < n - 1:
            term += 1
            fib = first + second
            first = second
            second = fib
        return fib
    
        



print fibonacci(7)

#print fibonacci(36)
#>>> 14930352