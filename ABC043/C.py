import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    ans = 10 ** 7
    for i in range(min(A), max(A)+1):
        c = sum([(a-i)**2 for a in A])
        ans = min(ans, c)
    
    print(ans)


if __name__ == '__main__':
    main()