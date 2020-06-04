import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7


def main():
    N = int(readline())
    A = readline().rstrip().replace(" ", "")
    print(int(A) % MOD)


if __name__ == "__main__":
    main()
