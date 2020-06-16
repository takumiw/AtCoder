import sys
readline = sys.stdin.readline
from collections import deque


def main():
    while True:
        N, M = map(int, readline().rstrip().split())
        if N == M == 0:
            break
        _, *A = map(int, readline().rstrip().split())
        _, *B = map(int, readline().rstrip().split())
        _, *C = map(int, readline().rstrip().split())

        A = [0] + A
        B = [0] + B
        C = [0] + C
        N += 1

        que = deque([(A, B, C, 0, -1)])   # pre: 1: A->B, 2: B->A, 3: B->C, 4: C->B
        res = -1
        while que:
            A, B, C, t, pre = que.popleft()
            if t > M:
                break
            if len(A) == N or len(C) == N:
                res = t
                break
            
            # A -> B
            if A[-1] > B[-1] and pre != 2:
                que.append((A[:-1], B + [A[-1]], C, t + 1, 1))

            # B -> A
            if B[-1] > A[-1] and pre != 1:
                que.append((A + [B[-1]], B[:-1], C, t + 1, 2))
            
            # B -> C
            if B[-1] > C[-1] and pre != 4:
                que.append((A, B[:-1], C + [B[-1]], t + 1, 3))
            
            # C -> B
            if C[-1] > B[-1] and pre != 3:
                que.append((A, B + [C[-1]], C[:-1], t + 1, 4))
            
        print(res)

if __name__ == '__main__':
    main()