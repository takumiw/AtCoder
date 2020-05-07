import sys
MOD = 10007

def main():
    N = int(sys.stdin.readline())
    a1, a2, a3 = 0, 0, 1
    if N <= 3:
        print([a1, a2, a3][N-1])
    else:
        for i in range(4, N+1):
            a1, a2, a3 = a2, a3, (a1+a2+a3) % MOD
        print(a3)

if __name__ == '__main__':
    main()