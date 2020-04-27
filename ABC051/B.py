import sys
readline = sys.stdin.readline

def main():
    K, S = map(int, readline().rstrip().split())
    ans = 0
    for x in range(K+1):
        for y in range(K+1):
            if 0 <= S - x - y <= K:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()