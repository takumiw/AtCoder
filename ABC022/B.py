import sys
readline = sys.stdin.readline
from collections import Counter

def main():
    N = int(readline())
    A = [int(readline()) for _ in range(N)]
    c = Counter(A)
    ans = 0
    for key, val in c.items():
        ans += (val - 1)
    
    print(ans)

if __name__ == '__main__':
    main()