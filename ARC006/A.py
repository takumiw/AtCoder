import sys
readline = sys.stdin.readline


def main():
    E = set(map(int, readline().rstrip().split()))
    B = int(readline())
    L = set(map(int, readline().rstrip().split()))

    if len(E & L) == 6:
        print(1)
    elif len(E & L) == 5:
        bonus = set(list(E) + [B])
        if len(bonus & L) == 6:
            print(2)
        else:
            print(3)
    elif len(E & L) == 4:
        print(4)
    elif len(E & L) == 3:
        print(5)
    else:
        print(0)    


if __name__ == '__main__':
    main()