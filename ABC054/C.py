import sys
readline = sys.stdin.readline
from collections import deque

def main():
    N, M = map(int, readline().rstrip().split())
    path = [[False] * N for _ in range(N)]
    for _ in range(M):
        a, b = map(int, readline().rstrip().split())
        path[a-1][b-1] = True
        path[b-1][a-1] = True
    
    que = deque([[0]])  # 訪れた順にノードを格納
    cnt = 0
    while que:
        visited = que.popleft()
        if len(visited) == N:
            cnt += 1
            continue
        pre = visited[-1]
        for next in range(N):
            if next not in visited and path[pre][next]:
                que.append(visited+[next])
            
    print(cnt)

if __name__ == '__main__':
    main()