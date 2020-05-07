import sys
readline = sys.stdin.readline

def main():
    N, M, C = map(int, readline().rstrip().split())
    B = list(map(int, readline().rstrip().split()))
    ans = 0
    for _ in range(N):
        A = list(map(int, readline().rstrip().split()))
        if sum([a*b for a, b in zip(A, B)]) + C > 0:
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()