N, K, Q = map(int, input().split())
A = [int(input())-1 for _ in range(Q)]

def solve():
    points = [0 for _ in range(N)]
    for a in A:
        points[a] += 1
    sum_points = sum(points)
    for p in points:
        if sum_points - p >= K:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    solve()