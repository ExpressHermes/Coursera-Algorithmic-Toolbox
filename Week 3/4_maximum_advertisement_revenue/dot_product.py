#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    # a, b = zip(*sorted(zip(a, b), key = lambda x: x[0] * x[1]))
    
    # res = 0
    a.sort()
    b.sort()
    return sum([x*y for x, y in zip(a, b)])
    
    # for i in range(len(a)):
    #     res += a[i] * b[i]
    # return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
