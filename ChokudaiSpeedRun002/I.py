import sys
readline = sys.stdin.readline


def main():
    N = int(readline())
    H, A = [], []
    for _ in range(N):
        h, a = map(int, readline().rstrip().split())
        H.append(h)
        A.append(a)

    res = 1
    str_h, str_a = H[0], A[0]
    for i in range(1, N):
        h, a = H[i], A[i]
        if -(-str_h // a) == -(-h // str_a):
            res = -1
        elif -(-str_h // a) < -(-h // str_a):
            res = i + 1
            str_h, str_a = h, a
    
    for i in range(N):
        if i + 1 == res:
            continue
        h, a = H[i], A[i]
        if -(-str_h // a) <= -(-h // str_a):
            res = -1
            break
    
    print(res)


if __name__ == '__main__':
    main()