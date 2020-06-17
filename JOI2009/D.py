import sys
readline = sys.stdin.readline
from itertools import permutations

def main():
    N = int(readline())
    K = int(readline())
    L = [int(readline()) for _ in range(N)]
    res = set()
    for l in permutations(L, K):
        res.add("".join(map(str, l)))
  
    print(len(res))

if __name__ == "__main__":
    main()
