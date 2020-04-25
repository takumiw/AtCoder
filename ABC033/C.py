import sys
readline = sys.stdin.readline

def main():
    S = readline().rstrip().split('+')
    cnt = 0
    for s in S:
        if '0' not in s:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()