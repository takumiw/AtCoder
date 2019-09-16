def solve():
    N = int(input())
    S = input()
    next_end = 1
    max_length = 0
    for start in range(N-1):
        for end in range(next_end, N):
            text = S[start:end]
            if text in S[end:]:
                max_length = max(len(text), max_length)
                continue
            else:
                if start + 1 == end:
                    next_end = end + 1
                else:
                    next_end = end
            break
    
    print(max_length)

if __name__ == '__main__':
    solve()