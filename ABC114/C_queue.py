import sys
readline = sys.stdin.readline
from collections import deque

def main():
    N = int(readline())
    que = []
    for val in ['357', '375', '537', '573', '735', '753']:
        if int(val) <= N:
            que.append(val)
    res = set(que)
    que = deque(que)
    while que:
        pre = que.popleft()
        for p in ['3', '5', '7']:
            for i in range(len(pre)+1):
                next = pre[:i] + p + pre[i:]
                if int(next) <= N and next not in res:
                    que.append(next)
                    res.add(next)

    print(len(res))

if __name__ == '__main__':
    main()