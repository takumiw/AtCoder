from collections import deque

def main():
    N = int(input())
    path = [[] for _ in range(N)]
    ab = []
    ans = {}
    visited = [False] * N
    visited[0] = True
    for _ in range(N-1):
        a, b = map(int, input().split())
        path[a-1].append(b-1)
        ab.append((a-1, b-1))
    
    que = deque([(0, 0)])
    while que:
        k = 1
        pre, c = que.popleft()
        for node in path[pre]:
            if visited[node]:
                continue
            if c == k:
                k += 1
            visited[node] = True
            ans[(pre, node)] = k
            que.append((node, k))
            k += 1

    print(max(ans.values()))
    print('\n'.join([str(ans[key]) for key in ab]))


if __name__ == '__main__':
    main()