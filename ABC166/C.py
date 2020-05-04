import sys
readline = sys.stdin.readline

def main():
    N, M = map(int, readline().rstrip().split())
    H = list(map(int, readline().rstrip().split()))
    Good = [1] * N
    for _ in range(M):
        a, b = map(int, readline().rstrip().split())
        a -= 1
        b -= 1
        if H[a] > H[b]:
            Good[b] = 0
        elif H[b] > H[a]:
            Good[a] = 0
        else:
            Good[a] = 0
            Good[b] = 0
    print(sum(Good))

if __name__ == '__main__':
    main()