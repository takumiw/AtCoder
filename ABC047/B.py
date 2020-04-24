import sys
readline = sys.stdin.readline

def main():
    W, H, N = map(int, readline().rstrip().split())
    p = [[1] * W for _ in range(H)]
    for _ in range(N):
        x, y, a = map(int, readline().rstrip().split())
        if a == 1:
            for yi in range(H):
                for xi in range(x):
                    p[yi][xi] = 0
        elif a == 2:
            for yi in range(H):
                for xi in range(x, W):
                    p[yi][xi] = 0
        elif a == 3:
            for xi in range(W):
                for yi in range(y):
                    p[yi][xi] = 0
        else:
            for xi in range(W):
                for yi in range(y, H):
                    p[yi][xi] = 0
    
    print(sum([sum(l) for l in p]))


if __name__ == '__main__':
    main()