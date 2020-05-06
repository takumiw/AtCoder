import sys
readline = sys.stdin.readline
from collections import deque
MOD = 10 ** 9 + 7
INF = 10 ** 10

def main():
    N = int(readline())
    a, b = map(int, readline().rstrip().split())
    a -= 1
    b -= 1
    M = int(readline())
    path = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, readline().rstrip().split())
        path[x-1].append(y-1)
        path[y-1].append(x-1)
    
    best = INF
    que = deque([[a]])
    while que:
        visited = que.popleft()
        pre = visited[-1]
        for next in path[pre]:
            if next in visited:
                continue
            if next == b:
                if len(visited) < best:
                    best = len(visited)
                    ans = 1
                elif len(visited) == best:
                    ans += 1
            else:
                que.append(visited+[next])
    
    print(ans % MOD)

if __name__ == '__main__':
    main()