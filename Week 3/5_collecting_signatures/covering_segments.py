# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    for s in segments:
        points.append((s.start, s.end))

    # sorting points based on right endpoint
    points.sort(key = lambda t: t[1])
    n = len(points)

    res = []

    while len(points):
        p = points[0][1]
        res.append(p)
        
        i = 0
        while i < len(points):
            if include(points[i], p):
                del points[i]
            else:
                i += 1
        
    return res

def include(point, p):
    if point[0] <= p and point[1] >= p:
        return True
    return False
    # print(points)
    # i = 0
    # res = set()
    # count = 0
    # while i < n: 
    #     if count == n:
    #         break
    #     print('\nLoop')
    #     gp = points[i][1]
    #     gp0 = points[i][0]
    #     print(f'Current Gp: {gp}, i: {i}')
        
        
    #     while i < n-1 and gp >= points[i+1][0] and points[i+1][0] != points[i+1][1]:
    #         i = i + 1
    #         continue
        
    #     print(f'i: {i}')
    #     if points[i+1][0] == points[i+1][1]:
    #         res.add(points[i+1][0])
    #     if i == n-1:
    #         res.add(min(gp, points[i][0]))
    #         break
    #     elif i > n - 1:
    #         break
    #     else:
    #         res.add(min(gp, points[i][0]))

        
    #     if gp < points[i+1][0] or points[i+1][0] == points[i+1][1]:
    #         i = i + 1
    #     print(f'Res: {res}')
    #     count += 1
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
