# Uses python3
import sys

def get_pisano_period(n):
    a, b, c = 0, 1, 1
    for _ in range(n*n):
        c = (a + b) % n
        a, b = b, c
        if a == 0 and b == 1:
            return _ + 1


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    # print("Calculating pisano period...")
    pisano = get_pisano_period(m)
    n = n % pisano
    # print(pisano, n)

    if n < 1:
        return 0
    else:
        for _ in range(n - 1):
            previous, current = current, previous + current

    # print(current)
    return current % m


def fibonacci_sum(n):
    if n <= 1:
        return n

    res = get_fibonacci_huge(n+2, 10) + 10
    # if res == 0:
    #     return res
    return (res - 1) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
