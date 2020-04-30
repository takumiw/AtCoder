import sys
readline = sys.stdin.readline
h1, w1 = map(int, readline().rstrip().split())
h2, w2 = map(int, readline().rstrip().split())
if h1 == h2 or w1 == w2 or h1 == w2 or w1 == h2:
    print('YES')
else:
    print('NO')