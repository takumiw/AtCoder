import sys
readline = sys.stdin.readline
from collections import Counter
MOD = 2019

def main():
    S = list(map(int, list(readline().rstrip())))
    N = len(S)
    T = [0] * (N+1)
    e = 1
    for i in range(N-1, -1, -1):
        T[i] = (T[i+1] + S[i] * e) % MOD
        e = e * 10 % MOD
    
    c = Counter(T)
    ans = 0
    for k, v in c.items():
        ans += (v * (v-1)) // 2
    print(ans)


if __name__ == '__main__':
    main()