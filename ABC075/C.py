import sys
readline = sys.stdin.readline
from collections import deque

def is_connected(path, N):
    visited = [False] * N
    visited[0] = True
    que = deque([0])
    while que:
        pre = que.popleft()
        for next in range(N):
            if not visited[next] and path[pre][next]:
                visited[next] = True
                que.append(next)
    
    if sum(visited) == N:
        return True
    else:
        return False

def main():
    N, M = map(int, readline().rstrip().split())
    path = [[False] * N for _ in range(N)]
    edge = []
    for _ in range(M):
        a, b = map(int, readline().rstrip().split())
        edge.append((a-1, b-1))
        path[a-1][b-1] = True
        path[b-1][a-1] = True
    
    res = 0
    for a, b in edge:
        path[a][b] = False
        path[b][a] = False

        if not is_connected(path, N):
            res += 1

        path[a][b] = True
        path[b][a] = True

    print(res)


if __name__ == '__main__':
    main()