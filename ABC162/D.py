def main():
    colors = ['R', 'G', 'B']
    N = int(input())
    S = input()
    
    ans = 0
    cnts = {'R': [], 'G': [], 'B': []}
    if S[-1] == 'R':
        cnts = {'R': [1], 'G': [0], 'B': [0]}
    elif S[-1] == 'G':
        cnts = {'R': [0], 'G': [1], 'B': [0]}
    else:
        cnts = {'R': [0], 'G': [0], 'B': [1]}

    for i, s in enumerate(S[::-1][1:]):
        for color in colors:
            if s == color:
                cnts[color].append(cnts[color][i] + 1)
            else:
                cnts[color].append(cnts[color][i])

    for color in colors:
        cnts[color] = cnts[color][::-1]

    for i in range(N-2):
        for j in range(i+1, N-1):
            if S[i] == S[j]:
                continue
            oth = colors[:]
            oth.remove(S[i])
            oth.remove(S[j])
            oth = oth[0]
            cnt = cnts[oth][j+1]
            ans += cnt
            if j + (j - i) < N:
                if S[j + (j - i)] == oth:
                    ans -= 1
            
    print(ans)


if __name__ == "__main__":
    main()