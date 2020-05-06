import sys
readline = sys.stdin.readline

def main():
    S = readline().rstrip()
    N = int(readline())
    for _ in range(N):
        l, r = map(int, readline().rstrip().split())
        S = S[:l-1] + S[l-1:r][::-1] + S[r:]

    print(S)

if __name__ == '__main__':
    main()