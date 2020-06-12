import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, readline().rstrip().split())
path = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, readline().rstrip().split())
    path[a-1].append(b-1)
    path[b-1].append(a-1)

def dfs(pre, now):
    global flg
    visited[now] = True
    for next in path[now]:
        if next == pre:
            continue
        if visited[next]:
            flg = False
            return
        dfs(now, next)

visited = [False] * N
res = 0
for s in range(N):
    if visited[s]:
        continue
    flg = True
    dfs(-1, s)
    if flg:
        res += 1
    
print(res)