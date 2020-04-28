import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    Ai = [a-i-1 for i, a in enumerate((A))]
    Ai.sort()
    if N % 2 == 1:
        b = Ai[N//2]
    else:
        b = (Ai[N//2-1] + Ai[N//2]) / 2

    print(int(sum([abs(a-b) for a in Ai])))


if __name__ == '__main__':
    main()