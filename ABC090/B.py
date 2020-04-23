import sys
readline = sys.stdin.readline

def main():
    A, B = map(int, readline().rstrip().split())
    ans = 0
    for i in range(A, B+1):
        if str(i) == str(i)[::-1]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()