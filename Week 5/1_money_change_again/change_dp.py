# Uses python3
import sys

def get_change(m):
    #write your code here
    a = [m+1]*(m+1)
    a[0], a[1] = 0, 1

    for i in range(2, m+1):
        if i >= 1:
            a[i] = min(a[i-1]+1, a[i])
        if i >= 3:
            a[i] = min(a[i-3]+1, a[i])
        if i >= 4:
            a[i] = min(a[i-4]+1, a[i])

    return a[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
