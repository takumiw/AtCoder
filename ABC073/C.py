import sys
readline = sys.stdin.readline
from collections import Counter

def main():
    N = int(readline())
    A = [int(readline()) for _ in range(N)]
    c = Counter(A)
    ans = 0
    for _, v in zip(c.keys(), c.values()):
        if v % 2 == 1:
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()