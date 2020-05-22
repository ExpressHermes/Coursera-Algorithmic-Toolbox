# Uses python3
import sys

def get_change(m):
    changes = 0

    while(m >= 10):
        # left = m % 10
        changes += m // 10
        m = m % 10

    while(m >= 5):
        # left = m % 5
        changes += m // 5
        m = m % 5

    return changes + m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
