import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    R = list(map(int, readline().rstrip().split()))
    R.sort()
    ans = 0
    for r in R[-K:]:
        ans = (ans + r) / 2
    
    print(ans)

if __name__ == '__main__':
    main()