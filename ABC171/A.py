import sys
readline = sys.stdin.readline


def main():
    a = readline().rstrip()
    if a.lower() == a:
        print("a")
    else:
        print("A")


if __name__ == '__main__':
    main()