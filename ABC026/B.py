import sys
readline = sys.stdin.readline
import math

def main():
    N = int(readline())
    R = [int(readline()) for _ in range(N)]
    R.sort(reverse=True)
    ans = 0
    for i, r in enumerate(R):
        if i % 2 == 0:
            ans += r ** 2 * math.pi
        else:
            ans -= r ** 2 * math.pi

    print(ans)


if __name__ == '__main__':
    main()