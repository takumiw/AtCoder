import sys
readline = sys.stdin.readline

def main():
    x = int(readline())
    ans = x // 11 * 2
    v = ans // 2 * 11
    if v < x:
        v += 6
        ans += 1
    if v < x:
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()