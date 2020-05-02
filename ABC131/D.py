import sys
readline = sys.stdin.readline
from operator import itemgetter

def main():
    N = int(readline())
    AB = [tuple(map(int, readline().rstrip().split())) for _ in range(N)]
    AB.sort(key=itemgetter(1))
    t = 0
    for a, b in AB:
        t += a
        if t > b:
            print('No')
            return
        
    print('Yes')

if __name__ == '__main__':
    main()