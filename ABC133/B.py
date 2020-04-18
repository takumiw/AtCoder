import sys
sys.setrecursionlimit(10 ** 6)


def calc_dist(x, y):
    dist = 0
    for xi, yi in zip(x, y):
        dist += (yi - xi) ** 2
    return dist ** (1/2)


def main():
    N, D = map(int, sys.stdin.readline().rstrip().split())
    X = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = calc_dist(X[i], X[j])
            if dist.is_integer():
                ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()