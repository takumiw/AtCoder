import sys
readline = sys.stdin.readline
import math

def main():
    X = int(readline())
    ans = 1
    for b in range(1, math.floor(X**(1/2))+1):
        for p in range(2, math.floor(math.log2(X))+1):
            if b ** p <= X:
                ans = max(ans, b ** p)
    
    print(ans)


if __name__ == '__main__':
    main()