import sys
readline = sys.stdin.readline
from operator import itemgetter

def main():
    N = int(readline())
    R = [tuple(map(int, readline().rstrip().split())) for _ in range(N)]
    B = [tuple(map(int, readline().rstrip().split())) for _ in range(N)]

    B.sort(key=itemgetter(0))
    R.sort(key=itemgetter(1), reverse=True)
    ans = 0
    for c, d in B:
        for a, b in R:
            if a < c and b < d:
                ans += 1
                R.remove((a, b))
                break
    
    print(ans)

if __name__ == '__main__':
    main()