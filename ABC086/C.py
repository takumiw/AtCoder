import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    res = 'Yes'
    pre_x, pre_y = 0, 0
    pre = 0
    for _ in range(N):
        t, x, y = map(int, readline().rstrip().split())
        cost = abs(x - pre_x) + abs(y - pre_y)
        if (t - pre) - cost >= 0 and ((t - pre) - cost) % 2 == 0:
            pre, pre_x, pre_y = t, x, y
        else:
            res = 'No'
            break

    print(res)

if __name__ == '__main__':
    main()