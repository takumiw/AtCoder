import sys
readline = sys.stdin.readline

def main():
    N, M = map(int, readline().rstrip().split())
    path = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, readline().rstrip().split())
        path[a-1].append(b-1)
        path[b-1].append(a-1)
    for i in range(N):
        print(len(path[i]))


if __name__ == '__main__':
    main()