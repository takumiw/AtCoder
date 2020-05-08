import sys
readline = sys.stdin.readline

def main():
    W, H, x, y = map(int, readline().rstrip().split())
    ans = W * H / 2
    if x == W / 2 and y == H / 2:
        mult = 1
    else:
        mult = 0
    print(ans, mult)


if __name__ == '__main__':
    main()