import sys
readline = sys.stdin.readline

def main():
    N, M = map(int, readline().rstrip().split())
    AB = [tuple(map(int, readline().rstrip().split())) for _ in range(N)]
    AB.sort()
    pro = 0
    cost = 0
    for a, b in AB:
        if pro + b >= M:
            cost += (M - pro) * a
            break
        pro += b
        cost += a * b
    
    print(cost)


if __name__ == '__main__':
    main()