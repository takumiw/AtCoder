import sys
readline = sys.stdin.readline

def main():
    S = list(map(int, list(readline().rstrip())))
    K = int(readline())

    if S[0] != 1 or len(S) == 1:
        print(S[0])
        return

    idx = min(len(S), K)
    if sum(S[:idx]) == len(S[:idx]):
        print(1)
    else:
        for e in S:
            if e != 1:
                print(e)
                return


if __name__ == '__main__':
    main()