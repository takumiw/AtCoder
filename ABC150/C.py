from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

def permutation(l, n):
    return [p for p in permutations(l, n)]

def main():
    perm = permutation([i for i in range(1, N+1)], N)
    a = perm.index(P)
    b = perm.index(Q)
    print(abs(a - b))

if __name__ == '__main__':
    main()