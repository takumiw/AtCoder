import sys
readline = sys.stdin.readline

def main():
    K = int(readline())
    S = readline().rstrip()
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')


if __name__ == '__main__':
    main()