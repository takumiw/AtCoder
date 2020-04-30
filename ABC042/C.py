import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    D = set(readline().rstrip().split())
    for i in range(N, N*10+1):
        d = str(i)
        flg = True
        for e in d:
            if e in D:
                flg = False
                break
        
        if flg:
            print(i)
            return


if __name__ == '__main__':
    main()