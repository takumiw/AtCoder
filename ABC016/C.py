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
        ans = set()
        for j in path[i]:
            for f in path[j]:
                if f != i and f not in path[i]:
                    ans.add(f)
        print(len(ans))


if __name__ == '__main__':
    main()