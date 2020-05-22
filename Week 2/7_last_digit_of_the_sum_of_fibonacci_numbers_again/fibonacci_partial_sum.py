# Uses python3
import sys

def fib_sum_fast(m, n):
    a = [0, 1]

    for i in range(2, 60):
        a.append((a[i-1] + a[i-2])%10)
    
    m = m % 60
    n = n % 60

    if n < m:
        n = n + 60

    s = 0
    for k in range(m, n + 1):
        s += a[k % 60]
    
    return s % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fib_sum_fast(from_, to))