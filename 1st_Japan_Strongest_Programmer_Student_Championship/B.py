N, K = map(int, input().split())
A = tuple(map(int, input().split()))
MOD = 10**9 + 7

def main():
    count1 = [0 for _ in range(N)]
    count2 = [0 for _ in range(N)]
    
    # 同じ整数列内での転倒数を数える
    for i, a in enumerate(A[:-1]):
        c = 0
        for b in A[i+1:]:
            if a > b:
                c += 1
        count1[i] = c

    # 異なる整数列に対する転倒数を数える
    for i, a in enumerate(A):
        c = 0
        for b in A[:i]:
            if a > b:
                c += 1
        count2[i] = c + count1[i]

    s = (sum(count1) * K) % MOD
    s += (sum(count2) * (K-1) * K // 2) % MOD
    print(s%MOD)
                
if __name__ == "__main__":
    main()
