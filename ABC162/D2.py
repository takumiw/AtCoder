def main():
    N = int(input())
    S = input()
    
    ans = S.count('R') * S.count('G') * S.count('B')
    for i in range(N-2):
        for j in range(i+1, i+1+(N-1-i)//2):
            k = j + (j - i)
            if S[i] != S[j] != S[k] != S[i]:
                ans -= 1
            
    print(ans)


if __name__ == "__main__":
    main()