def cached_execution(cache, proc, proc_input):
    # Your code here
    #print ("the inputs are {}, {}".format(proc,proc_input))
    if proc not in cache:
        #print ("oh something new!")
        cache[proc] = proc(proc_input)
        return cache[proc]
    else:
        #print ("its already in our db")
        return cache[proc]
        
def factorial(n):
    print ("Running factorial")
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


cache = {}

def cached_fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return (cached_execution(cache, cached_fibo, n - 1 )
               + cached_execution(cache,  cached_fibo, n - 2 ))
               
 # new cache for this procedure
# do not try this at home...at least without a cache!
### first execution (should print out Running factorial and the result)
print (cached_execution(cache, factorial, 50))


### second execution (should only print out the result)
print (cached_execution(cache, factorial, 50))
print (cached_execution(cache, cached_fibo,100))