import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    S = list(map(int, list(readline().rstrip())))

    cnt = []
    pre = S[0]
    S.append(-1)
    c = 1
    for s in S[1:]:
        if s == pre:
            c += 1
        else:
            cnt.append(c)
            pre = s
            c = 1
    
    if S[0] == 0:
        cnt = [0] + cnt
    if S[-2] == 0:
        cnt.append(0)
    
    K = K * 2 + 1
    ans = sum(cnt[:K])
    sc = ans
    for i in range(2, len(cnt)-K+1, 2):
        sc = sc - cnt[i-1] - cnt[i-2] + cnt[i+K-1] + cnt[i+K-2]
        ans = max(ans, sc)

    print(ans)

if __name__ == '__main__':
    main()