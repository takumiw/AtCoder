import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    res = 1 * (K-1) * (N-K) * 6 + (K-1) * 3 + (N-K) * 3 + 1
    print(res / N**3)

if __name__ == '__main__':
    main()