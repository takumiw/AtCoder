import time, random

def main():
    """N = int(input())
    P = list(map(int, input().split()))"""
    start = time.time()
    N = 2 * 10**5
    P = [random.randint(1, 100000) for _ in range(N)]

    ans = 1
    min_val = P.pop(0)
    for p in P:
        if p <= min_val:
            ans += 1
            min_val = p

    print(ans)
    print(time.time()-start)

if __name__ == '__main__':
    main()