import sys
readline = sys.stdin.readline

def main():
    S = readline().rstrip()
    N = len(S)
    ans = 0
    for i in range(2**(N-1)):
        b = bin(i)[2:].zfill(N-1)
        f = [S[i]+'+' if b[i]=='1' else S[i] for i in range(N-1)]
        f += S[-1]
        ans += eval(''.join(f))
    
    print(ans)


if __name__ == '__main__':
    main()