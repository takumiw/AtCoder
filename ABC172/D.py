import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    res = 0
    for x in range(1, N+1):
        y = N // x
        res += y * (y + 1) * x // 2
    
    print(res)

if __name__ == '__main__':
    main()