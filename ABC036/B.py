import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    inp = [readline().rstrip() for _ in range(N)]
    ans = [[None]*N for _ in range(N)]
    for j in range(N):
        for i in range(N-1, -1, -1):
            ans[j][N-i-1] = inp[i][j]
    
    ans = [''.join(l) for l in ans]
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()