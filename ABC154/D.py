def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    P = [(1+p)/2 for p in P]
    p_sum = [sum(P[:K])]
    for i in range(K, N):
        p_sum.append(p_sum[-1] - P[i-K] + P[i])

    print(max(p_sum))

if __name__ == '__main__':
    main()