import sys
readline = sys.stdin.readline

def main():
    N, M, Q = map(int, readline().rstrip().split())
    path = [[False]* N for _ in range(N)]
    for _ in range(M):
        u, v = map(int, readline().rstrip().split())
        path[u-1][v-1] = True
        path[v-1][u-1] = True
    
    color = list(map(int, readline().rstrip().split()))
    for _ in range(Q):
        input_line = list(map(int, readline().rstrip().split()))
        if len(input_line) == 2:
            x = input_line[1] - 1
            c = color[x]
            print(c)
            for i in range(N):
                if path[x][i]:
                    color[i] = c
        elif len(input_line) == 3:
            x = input_line[1] - 1
            y = input_line[2]
            print(color[x])
            color[x] = y


if __name__ == '__main__':
    main()