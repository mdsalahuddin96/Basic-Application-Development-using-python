def list_fib(n):
    fib_list=[1,1]
    if n<=2:
        return fib_list[:n]
    fib_x,fib_next=1,1
    i=3
    while i<=n:
        i+=1
        fib_x,fib_next=fib_next,fib_x+fib_next
        fib_list.append(fib_next)
    return fib_list