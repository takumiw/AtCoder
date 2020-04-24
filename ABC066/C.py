import sys
readline = sys.stdin.readline
from collections import deque

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    que = deque([])
    for i, a in enumerate(A):
        if i % 2 == 0:
            que.append(a)
        else:
            que.appendleft(a)
    
    if N % 2 == 1:
        que = list(que)[::-1]
    print(*que)


if __name__ == '__main__':
    main()