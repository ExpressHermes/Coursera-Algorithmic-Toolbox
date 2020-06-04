# Uses python3
import sys
import random

# Random quick sort using The Dutch National Flag problem
# Make two passes to sort the given sub array
# In first pass, move all the elements < value in the starting
# of array.
# In second pass, move all the elements > value in the last 
# of array

def partition3(a, l, r):
    placement = l
    value = a[l]

    # First pass
    for i in range(l, r):
        if a[i] < value:
            a[i], a[placement] = a[placement], a[i]
            placement += 1

    m1 = placement
    placement = r-1

    # Second pass
    for i in range(r-1, l-1, -1):
        if a[i] > value:
            a[i], a[placement] = a[placement], a[i]

        if a[i]  < value:
            break

    
    m2 = placement
    return m1, m2

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1);
    randomized_quick_sort(a, m2+1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
