import sys
readline = sys.stdin.readline
from collections import Counter

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    c = Counter(A)
    mi = min(A)+1
    m = c[mi-1] + c[mi] + c[mi+1]
    ans = m
    for i in range(mi+1, max(A)):
        m -= c[i-2]
        m += c[i+1]
        ans = max(ans, m)
    
    print(ans)


if __name__ == '__main__':
    main()
