import sys
readline = sys.stdin.readline
from collections import Counter

def main():
    N = int(readline())
    S = [readline().rstrip() for _ in range(N)]
    c = Counter(S)
    print(c.most_common()[0][0])

if __name__ == '__main__':
    main()