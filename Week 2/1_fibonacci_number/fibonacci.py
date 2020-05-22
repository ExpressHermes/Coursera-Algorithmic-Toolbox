# Uses python3
def calc_fib(n):
    fib = list(None for x in range(50))
    fib[0] = 0
    fib[1] = 1

    if fib[n]:
        return fib[n]
    else:
        for i in range(2, n+1):
            fib[i] = fib[i-1] + fib[i-2]

        return fib[n]


n = int(input())
print(calc_fib(n))
