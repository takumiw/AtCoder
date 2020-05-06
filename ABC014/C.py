import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    cnt = [0] * (10**6+2)
    for _ in range(N):
        a, b = map(int, readline().rstrip().split())
        cnt[a] += 1
        cnt[b+1] -= 1
    for i in range(10**6):
        cnt[i+1] += cnt[i]
    
    print(max(cnt))

if __name__ == '__main__':
    main()