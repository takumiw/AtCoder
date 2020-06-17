import sys
readline = sys.stdin.readline
from itertools import permutations
from math import factorial

def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    cnt = 0
    
    for l1 in permutations(A, N):
        for l2 in permutations(B, N):
            if len([1 for a, b in zip(l1, l2) if a > b]) > N/2:
                cnt += 1
     
  
    print(cnt / (factorial(N) ** 2))

if __name__ == "__main__":
    main()
