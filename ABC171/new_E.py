import sys
readline = sys.stdin.readline


def main():
    N = int(readline())  # 偶数
    A = list(map(int, readline().rstrip().split()))  # [自分以外の全ての整数のxor, ...]
    
    xor = 0
    for a in A:
        xor ^= a
    
    res = [a ^ xor for a in A]
    print(*res)


if __name__ == '__main__':
    main()