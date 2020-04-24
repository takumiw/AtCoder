import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = [int(readline()) - 1 for _ in range(N)]
    ans = 0
    pre = 0
    visited = set([0])
    while ans <= N:
        pre = A[pre]
        if pre in visited:
            print(-1)
            return
        visited.add(pre)
        ans += 1
        if pre == 1:
            print(ans)
            return
    
    print(-1)
    return


if __name__ == '__main__':
    main()