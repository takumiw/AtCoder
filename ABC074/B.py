import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    K = int(readline())
    X = list(map(int, readline().rstrip().split()))
    ans = 0
    for x in X:
        ans += min(x*2, abs(x-K)*2)
    print(ans)

if __name__ == '__main__':
    main()