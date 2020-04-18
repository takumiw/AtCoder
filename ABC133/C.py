import sys
sys.setrecursionlimit(10 ** 6)

def main():
    L, R = map(int, sys.stdin.readline().rstrip().split())

    if (R // 2019) > (L // 2019):
        print(0)
        exit()

    L %= 2019
    R %= 2019
    ans = 2019
    for i in range(L, R+1):
        for j in range(i+1, R+1):
            ans = min(ans, (i*j) % 2019)
    
    print(ans)


if __name__ == '__main__':
    main()