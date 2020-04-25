import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    idx = [i for i in range(1, N+1)]
    z = zip(A, idx)
    z = sorted(z, reverse=True)
    A, idx = zip(*z)
    print(*idx, sep='\n')

if __name__ == '__main__':
    main()