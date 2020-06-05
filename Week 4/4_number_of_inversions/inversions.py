# Uses python3
import sys

inversion_count = 0
def merge(p, q):
    i, j = 0, 0
    global inversion_count
    c = []
    while i < len(p) and j < len(q):
        if p[i] > q[j]:
            inversion_count += len(p) - i
            c.append(q[j])
            j += 1
        else:
            c.append(p[i])
            i += 1
    
    while i < len(p):
        c.append(p[i])
        i += 1
    
    while j < len(q):
        c.append(q[j])
        j += 1
    
    return c

def merge_sort(a):
    if len(a) == 1:
        return a

    mid = len(a) // 2
    p = merge_sort(a[:mid])
    q = merge_sort(a[mid:])
    return merge(p, q)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    merge_sort(a)
    print(inversion_count)
