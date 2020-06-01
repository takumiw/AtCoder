import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    res = 1
    A = list(map(int, readline().rstrip().split()))
    if 0 in A:
        print(0)
        return
    for a in A:
        res *= a
        if res > 10 ** 18:
            print(-1)
            return

    print(res)
    

if __name__ == '__main__':
    main()