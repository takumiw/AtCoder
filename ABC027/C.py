import sys
readline = sys.stdin.readline
import math

def main():
    N = int(readline())
    x = 1
    depth = 0
    n = N
    while n > 1:
        depth += 1
        n //= 2

    if depth % 2 == 0:
        for i in range(100):
            if i % 2 == 0:
                x = x * 2 + 1
            else:
                x *= 2
            if x > N:
                break
    else:
        for i in range(100):
            if i % 2 == 1:
                x = x * 2 + 1
            else:
                x *= 2
            if x > N:
                break
    
    if i % 2 == 0:
        print('Aoki')
    else:
        print('Takahashi')


if __name__ == '__main__':
    main()