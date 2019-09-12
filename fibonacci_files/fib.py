def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for i in range(1,41):
    print(i, ". fibonacci: ", fib(i))





















































#also works

def nem(n):
    if n < 1:
        return 1
    return em(n-1)

def em(n):
    if n < 1:
        return 1
    s = 1
    for i in range(n):
        s += nem(i)
    return s

def fib2(n):
    f = [0,1,1]
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
    return f[n]

#for i in range(1,41):
#    print(i, '. fibonacci: ', fib2(i))
