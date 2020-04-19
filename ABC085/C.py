import sys

def main():
    N, Y = map(int, sys.stdin.readline().rstrip().split())

    for n in range(Y//10000+1):
        for m in range((Y-n*10000)//5000+1):
            l = N - n - m
            if l >= 0 and n*10000 + m*5000 + l*1000 == Y:
                print(n, m, l)
                return
    
    print(-1, -1, -1)


if __name__ == '__main__':
    main()