import sys, math
sys.setrecursionlimit(10 ** 6)
from collections import deque, defaultdict, Counter
from operator import itemgetter

def main():
    N, M, X = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    
    idx = -1
    for i in range(M+1):
        if A[i] < X:
            idx = i
        else:
            break
    
    print(min(len(A[:idx+1]), len(A[idx+1:])))


if __name__ == '__main__':
    main()