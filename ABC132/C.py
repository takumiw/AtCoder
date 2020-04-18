import sys
sys.setrecursionlimit(10 ** 6)

def main():
    N = int(input())
    D = list(map(int, sys.stdin.readline().rstrip().split()))
    D.sort()
    print(max(0, D[N//2]-D[N//2-1]))


if __name__ == '__main__':
    main()