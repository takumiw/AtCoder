import sys
readline = sys.stdin.readline
from fractions import gcd

def main():
    N, X = map(int, readline().rstrip().split())
    x = list(map(int, readline().rstrip().split()))
    x = [abs(e-X) for e in x]
    
    if N == 1:
        print(x[0])
        return
    
    g = gcd(x[0], x[1])
    if N == 2:
        print(g)
        return

    for e in x[2:]:
        g = gcd(g, e)
    
    print(g)  


if __name__ == '__main__':
    main()