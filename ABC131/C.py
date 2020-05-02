import sys
readline = sys.stdin.readline
import fractions

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def main():
    A, B, C, D = map(int, readline().rstrip().split())
    CD = lcm_base(C, D)
    ans = B - (B//C + B//D - B//CD)
    ans -= ((A-1) - ((A-1)//C + (A-1)//D - (A-1)//CD))
    print(ans)

if __name__ == '__main__':
    main()