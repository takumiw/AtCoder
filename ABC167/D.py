import sys
readline = sys.stdin.readline

def main():
    N, K = map(int, readline().rstrip().split())
    A = list(map(int, readline().rstrip().split()))
    if K <= N:
        pre = 1
        for _ in range(K):
            pre = A[pre-1]
        print(pre)
        return

    pre = 1
    visited_set = set([1])
    visited = [1]
    for i in range(N):
        pre = A[pre-1]
        if pre in visited_set:
            break
        visited_set.add(pre)
        visited.append(pre)
    
    loop_start = visited.index(pre)
    loop = i - loop_start + 1

    num_loop = (K - loop_start) // loop
    now = loop_start + num_loop * loop
    for i in range(now+1, K+1):
        pre = A[pre-1]
    
    print(pre)

if __name__ == '__main__':
    main()