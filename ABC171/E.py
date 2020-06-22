import sys
readline = sys.stdin.readline


def main():
    N = int(readline())  # 偶数
    A = list(map(int, readline().rstrip().split()))  # [自分以外の全ての整数のxor, ...]
    
    if N == 2:
        print(*A[::-1])
        return
    
    xor = []
    for i in range(N-1):
        xor.append(A[i] ^ A[i+1])  # a xor b, b xor c, c xor d ...
    
    # bを求める
    b = A[0]
    for i in range(2, N, 2):
        b ^= xor[i]
    
    # aを求める
    a = xor[0] ^ b

    res = [a, b]
    pre = b

    # c以降を求める
    for x in xor[1:]:
        next = pre ^ x
        res.append(next)
        pre = next

    
    print(*res)


if __name__ == '__main__':
    main()