def main():
    N = int(input())

    freq = {}
    for i in range(1, N+1):
        pair = str(i)[0] + str(i)[-1]
        freq.setdefault(pair, 0)
        freq[pair] += 1
    
    ans = 0
    for i in range(1, N+1):
        pair_rev = str(i)[-1] + str(i)[0]
        if pair_rev in freq.keys():
            ans += freq[pair_rev]
    
    print(ans)    


if __name__ == "__main__":
    main()