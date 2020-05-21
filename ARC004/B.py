import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    D = [int(readline()) for _ in range(N)]
    D.sort(reverse=True)
    res_max = sum(D)
    if len(D) == 1:
        res_min = D[0]
    else:
        if sum(D[1:]) >= D[0]:
            res_min = 0
        else:
            res_min = D[0] - sum(D[1:])

    print(res_max)
    print(res_min)

if __name__ == '__main__':
    main()