import sys
readline = sys.stdin.readline

def main():
    N, X = map(int, readline().rstrip().split())
    L = list(map(int, readline().rstrip().split()))
    ans = 1
    d = 0
    for l in L:
        d += l
        if d <= X:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()