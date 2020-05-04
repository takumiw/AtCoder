import sys
readline = sys.stdin.readline
import math

def main():
    N, K = map(int, readline().rstrip().split())
    S = [0] * N
    for _ in range(K):
        d = int(readline())
        A = list(map(int, readline().rstrip().split()))
        for a in A:
            S[a-1] += 1
    
    print(len([s for s in S if s == 0]))


if __name__ == '__main__':
    main()