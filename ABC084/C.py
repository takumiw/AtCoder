import sys
readline = sys.stdin.readline
import math

def main():
    N = int(readline())
    CSF = [list(map(int, readline().rstrip().split())) for _ in range(N-1)]
    
    for i in range(N):
        t = 0
        for c, s, f in CSF[i:]:
            m = (t - s) / f
            m = max(math.ceil(m), 0)
            t = s + f * m + c
        print(t)


if __name__ == '__main__':
    main()