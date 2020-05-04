import sys
readline = sys.stdin.readline
from collections import Counter

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    A1 = [i + a for i, a in enumerate(A)]
    A2 = [i - a for i, a in enumerate(A)]
    c1 = Counter(A1)
    c2 = Counter(A2)
    c2_keys = c2.keys()
    ans = 0
    for key, val in c1.items():
        if key in c2_keys:
            ans += val * c2[key]

    print(ans)

if __name__ == '__main__':
    main()