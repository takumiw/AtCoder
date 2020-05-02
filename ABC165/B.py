import sys
readline = sys.stdin.readline
import math

def main():
    X = int(readline())
    ans = 100
    cnt = 0
    while ans < X:
        ans += math.floor(ans * 0.01)
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()