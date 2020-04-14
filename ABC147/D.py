MOD = 10 ** 9 + 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    max_bin_digits = len(bin(max(A))[2:])
    ans = 0
    for i in range(max_bin_digits):
        cnt = 0
        m = 1 << i
        for a in A:
            if m & a:
                cnt += 1
        
        ans += cnt * (N - cnt) * m
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()