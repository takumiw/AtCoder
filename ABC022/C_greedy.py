import sys
readline = sys.stdin.readline
from collections import deque

def main():
    N, M = map(int, readline().rstrip().split())
    path = [[] for _ in range(N)]
    for _ in range(M):
        u, v, l = map(int, readline().rstrip().split())
        path[u-1].append((v-1, l))
        path[v-1].append((u-1, l))

    visited_all = deque([([0], 0)])
    ans = 10 ** 10
    while visited_all:
        visited, dist = visited_all.popleft()
        pre = visited[-1]
        for next, l in path[pre]:
            if len(visited) > 2 and next == 0:
                ans = min(ans, dist+l)
                continue
            if next not in visited:
                visited_all.append((visited + [next], dist+l))
    
    if ans == 10 ** 10:
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()