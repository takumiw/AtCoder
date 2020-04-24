import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    L = list(map(int, readline().rstrip().split()))
    L.sort(reverse=True)
    print(sum(L[:K]))
    

if __name__ == '__main__':
    main()