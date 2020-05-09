import sys
readline = sys.stdin.readline
from collections import deque

def main():
    N = int(readline())
    path = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b, c = map(int, readline().rstrip().split())
        path[a-1].append((b-1, c))
        path[b-1].append((a-1, c))
    Q, K = map(int, readline().rstrip().split())
    K -= 1

    dist = [-1] * N
    dist[K] = 0
    
    que = deque([K])
    while que:
        pre = que.popleft()
        for next, d in path[pre]:
            if dist[next] == -1:
                dist[next] = dist[pre] + d
                que.append(next)

    for _ in range(Q):
        x, y = map(int, readline().rstrip().split())
        print(dist[x-1] + dist[y-1])

if __name__ == '__main__':
    main()