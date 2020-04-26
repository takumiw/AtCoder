import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    S = [readline().rstrip() for _ in range(N)]
    print(len(set(S)))


if __name__ == '__main__':
    main()