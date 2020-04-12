import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def main():
    K = int(input())
    ans = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            for k in range(1, K+1):
              ans += gcd(i, j, k)

    print(ans)

if __name__ == "__main__":
    main()