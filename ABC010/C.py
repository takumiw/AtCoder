import sys
readline = sys.stdin.readline

def main():
    xa, ya, xb, yb, T, V = map(int, readline().rstrip().split())
    ma = T * V
    N = int(readline())
    for _ in range(N):
        x, y = map(int, readline().rstrip().split())
        if ((x-xa)**2 + (y-ya)**2)**(1/2) + ((x-xb)**2 + (y-yb)**2)**(1/2) <= ma:
            print('YES')
            return
    
    print('NO')
    return


if __name__ == '__main__':
    main()