import sys
readline = sys.stdin.readline
from collections import Counter

def main():
    S = readline().rstrip()
    N = len(S)
    c = Counter(S)
    cnt_odd = len([1 for v in c.values() if v % 2 == 1])
    
    if cnt_odd == 0:
        print(N)

    else:
        print(2 * ((N - cnt_odd) // (2 * cnt_odd)) + 1)
    
if __name__ == '__main__':
    main()