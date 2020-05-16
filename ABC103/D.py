import sys
readline = sys.stdin.readline
from operator import itemgetter

def main():
    N, M = map(int, readline().rstrip().split())
    AB = [tuple(map(int, readline().rstrip().split())) for _ in range(M)]
    AB.sort(key=itemgetter(1))
    res = 1
    x = AB[0][1] - 2
    for a, b in AB[1:]:
        if a - 1 <= x:
            continue
        res += 1
        x = b - 2
    
    print(res)


if __name__ == '__main__':
    main()