import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = [int(readline()) for _ in range(N)]
    A_desc = sorted(set(A))
    d = {a: i for i, a in enumerate(A_desc)}
    for a in A:
        print(d[a])


if __name__ == '__main__':
    main()