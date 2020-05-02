import sys
readline = sys.stdin.readline
from itertools import combinations_with_replacement

def main():
    N, M, Q = map(int, readline().rstrip().split())
    P = [tuple(map(int, readline().rstrip().split())) for _ in range(Q)]
    ans = 0    
    for pair in combinations_with_replacement([i for i in range(1, M+1)], N):
        score = 0
        for a, b, c, d in P:
            if pair[b-1] - pair[a-1] == c:
                score += d
        ans = max(ans, score)
    
    print(ans)

if __name__ == '__main__':
    main()