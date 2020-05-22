# Uses python3
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fib_fast(n):
    fib = [-1 for x in range(n+2)]
    fib[0] = 0
    fib[1] = 1

    if fib[n] != -1:
        return sum([fib[x] for x in range(n + 1)]) % 10


    else:
        for i in range(2, n+1):
            fib[i] = (fib[i-1] % 10 + fib[i-2] % 10) % 10
        return sum([fib[x] % 10 for x in range(n + 1)]) % 10


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(get_fib_fast(i))
