import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    P = list(map(int, readline().rstrip().split()))
    P.sort()

    print(sum(P[:K]))
    
if __name__ == '__main__':
    main()