from collections import deque

def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1

    ans = [0 for _ in range(N)]
    for s in range(N):
        dist = [-1 for _ in range(N)]
        dist[s] = 0

        d = deque([s])
        while(len(d) > 0):
            v = d.popleft()
            if v == X:
                if dist[Y] == -1:
                    d.append(Y)
                    dist[Y] = dist[v] + 1
            elif v == Y:
                if dist[X] == -1:
                    d.append(X)
                    dist[X] = dist[v] + 1
            if v + 1 < N:
                if dist[v+1] == -1:
                    d.append(v+1)
                    dist[v+1] = dist[v] + 1
            if v - 1 >= 0:
                if dist[v-1] == -1:
                    d.append(v-1)
                    dist[v-1] = dist[v] + 1

        for i in range(N):
            ans[dist[i]] += 1
 
    for k in range(1, N):
        print(ans[k] // 2)


if __name__ == "__main__":
    main()