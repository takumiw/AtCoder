import sys
readline = sys.stdin.readline
from operator import itemgetter

def main():
    N = int(readline())
    SP = []
    for i in range(N):
        s, p = readline().rstrip().split()
        SP.append((s, int(p), i+1))
    SP.sort(key=itemgetter(1), reverse=True)
    SP.sort(key=itemgetter(0))
    for i in range(N):
        print(SP[i][2])

if __name__ == '__main__':
    main()