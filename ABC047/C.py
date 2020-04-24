import sys
readline = sys.stdin.readline

def main():
    S = list(readline().rstrip())
    ans = 0
    for i in range(1, len(S)):
        if S[i-1] != S[i]:
            ans += 1
    
    print(ans)


if __name__ == '__main__':
    main()