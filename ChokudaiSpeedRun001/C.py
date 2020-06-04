import sys

readline = sys.stdin.readline


def main():
    N = int(readline())
    l = readline().rstrip().split()
    print(*(l), sep=",")


if __name__ == "__main__":
    main()
