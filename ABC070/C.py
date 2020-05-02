import sys
readline = sys.stdin.readline
from fractions import gcd

def main():
    N = int(readline())
    ans = 1
    for _ in range(N):
        t = int(readline())
        ans = (ans * t) // gcd(ans, t)
    
    print(ans)
    
if __name__ == '__main__':
    main()