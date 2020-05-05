import sys
readline = sys.stdin.readline
from collections import Counter

def main():
    w = readline().rstrip()
    c = Counter(w)
    for key, val in c.items():
        if val % 2 == 1:
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()