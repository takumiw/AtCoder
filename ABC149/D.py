def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = list(input())

    score = 0
    for i in range(K, N):
        if T[i] == T[i-K]:
            T[i] = 'x'
    
    for t in T:
        if t == 'r':
            score += P
        elif t == 's':
            score += R
        elif t == 'p':
            score += S
    
    print(score)


if __name__ == "__main__":
    main()