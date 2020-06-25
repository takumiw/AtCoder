import sys
readline = sys.stdin.readline
MOD = 10 ** 9 + 7

N = int(readline())
path = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, readline().rstrip().split())
    path[a-1].append(b-1)
    path[b-1].append(a-1)

W = [0] * N
B = [0] * N

def dfs(pre, cur):
    W[cur] = B[cur] = 1
    for next in path[cur]:
        if next == pre:
            continue
        dfs(cur, next)
        W[cur] *= (W[next] + B[next]) % MOD
        B[cur] *= W[next] % MOD


def main():
    dfs(-1, 0)
    print((W[0] + B[0]) % MOD)


if __name__ == '__main__':
    main()