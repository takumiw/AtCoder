import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    res = 0
    for _ in range(N):
        a, b = map(int, readline().rstrip().split())
        res += min(a // 2, b)
    
    print(res)

if __name__ == '__main__':
    main()