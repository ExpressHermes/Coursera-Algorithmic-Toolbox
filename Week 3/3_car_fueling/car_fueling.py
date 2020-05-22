# python3
import sys

def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    stops.insert(0, 0)
    n = len(stops)
    # print(n-1)
    dist_covered = 0
    i = 0
    prev_stop = i
    refill = 0

    while i < n:
        # print('\nLoop starts')
        prev_stop = i

        # print(f'Prev_stop: {prev_stop}, i: {i}')
        while i < n and stops[i] - stops[prev_stop] <= tank:
            i += 1

        i = i - 1
        # print(f'i: {i}')
        if i == prev_stop and i != n-1:
            return -1

        if i < n-1:
            refill += 1
        else:
            break
        # print(f'Refill: {refill}')
    return refill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
