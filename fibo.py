# 0 1 1 2 3 5 8 13 21

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# print(fib(8))

def fibmemo(n, d = {}):
    print(d,n)
    if n in d: return d[n]
    if n <= 2: return 1
    d[n] = fibmemo(n-1, d) + fibmemo(n-2, d)
    return d[n]
print(fibmemo(10))

def fiboevensummer():
    
    fibolist = [1,2]  #initial start
    evensum = 2

    maxval = 0
    count = 1  #start to append
    while maxval < 4000000:
        maxval = fibolist[count] + fibolist[count-1]
        fibolist.append(maxval)
        # print(maxval)
        if maxval % 2 == 0 :
            evensum += maxval
        count += 1

    print(evensum)
fiboevensummer()

    
