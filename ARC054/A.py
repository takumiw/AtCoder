import sys
readline = sys.stdin.readline

def main():
    L, X, Y, S, D = map(int, readline().rstrip().split())

    # 時計回りに進む場合
    if S >= D:
        d = (L - S) + D
    else:
        d = D - S
    res = d / (X + Y)

    # 反時計回りに進む場合
    if Y > X:
        if S >= D:
            d = S - D
        else:
            d = S + (L - D)
        res = min(res, d / (Y - X))

    print(res)


if __name__ == '__main__':
    main()