import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    T, A = map(int, readline().rstrip().split())
    H = list(map(int, readline().rstrip().split()))
    temp = [T - x*0.006 for x in H]
    d = 10 ** 5
    res = -1
    for i, t in enumerate(temp):
        if abs(A - t) < d:
            res = i + 1
            d = abs(A - t)
    
    print(res)


if __name__ == '__main__':
    main()