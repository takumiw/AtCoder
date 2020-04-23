import sys
readline = sys.stdin.readline
from collections import Counter

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    c = Counter(A)
    A = [a for a in A if c[a] > 1]
    if len(A) < 4:
        print(0)
        exit()
    c = Counter(A)
    keys = c.keys()
    vals = c.values()
    z = zip(keys, vals)
    z = sorted(z, reverse=True)
    keys, vals = zip(*z)
    if vals[0] >= 4:
        a1, a2 = keys[0], keys[0]
    else:
        a1, a2 = keys[0], keys[1]
    print(a1 * a2)


if __name__ == '__main__':
    main()