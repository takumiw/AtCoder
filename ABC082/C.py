import sys
readline = sys.stdin.readline
from collections import Counter

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    c = Counter(A)
    ans = 0
    for k, v in zip(c.keys(), c.values()):
        if v - k >= 0:
            ans += v - k
        else:
            ans += v
    
    print(ans)


if __name__ == '__main__':
    main()