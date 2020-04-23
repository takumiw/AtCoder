import sys
readline = sys.stdin.readline

def main():
    N = int(input())
    cnt = [0, 0, 0, 0, 0]
    for _ in range(N):
        s = input()
        if s[0] == 'M':
            cnt[0] += 1
        elif s[0] == 'A':
            cnt[1] += 1
        elif s[0] == 'R':
            cnt[2] += 1
        elif s[0] == 'C':
            cnt[3] += 1
        elif s[0] == 'H':
            cnt[4] += 1
    
    ans = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                ans += cnt[i] * cnt[j] * cnt[k]
    
    print(ans)


if __name__ == '__main__':
    main()