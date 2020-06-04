# Uses python3
import sys

# After sorting, majority element, if it exists, will
# always be the middle element of n array
def get_majority_element(a, left, right):
    a.sort()
    element = a[len(a)//2]  
    if sum(1 for x in a if x == element) > n//2:
        return element
    else:
       return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
