import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    if N == 0:
        print(0)
        return
    ans = []
    i = 0
    while N:
        if N % 2 == 0:
            ans.append(0)
            N //= 2
        else:
            ans.append(1)
            if i % 2 == 0:
                N -= 1
            else:
                N += 1
            N //= 2
        i += 1

    print(*ans[::-1], sep='')

if __name__ == '__main__':
    main()