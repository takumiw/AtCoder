import sys
readline = sys.stdin.readline
from fractions import gcd

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))

    l = lcm_base(A[0], A[1])
    for a in A[2:]:
        l = lcm_base(l, a)
    
    l -= 1
    print(sum([l % a for a in A]))


if __name__ == '__main__':
    main()