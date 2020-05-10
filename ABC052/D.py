import sys
readline = sys.stdin.readline

def main():
    N, A, B = map(int, readline().rstrip().split())
    X = list(map(int, readline().rstrip().split()))
    res = 0
    for i in range(N-1):
        res += min((X[i+1] - X[i]) * A, B)
    
    print(res)

if __name__ == '__main__':
    main()