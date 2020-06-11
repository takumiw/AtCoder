import sys
readline = sys.stdin.readline

def check(s):
    if s == ['###', '#.#', '#.#', '#.#', '###']:
        return 0
    elif s == ['.#.', '##.', '.#.', '.#.', '###']:
        return 1
    elif s == ['###', '..#', '###', '#..', '###']:
        return 2
    elif s == ['###', '..#', '###', '..#', '###']:
        return 3
    elif s == ['#.#', '#.#', '###', '..#', '..#']:
        return 4
    elif s == ['###', '#..', '###', '..#', '###']:
        return 5
    elif s == ['###', '#..', '###', '#.#', '###']:
        return 6
    elif s == ['###', '..#', '..#', '..#', '..#']:
        return 7
    elif s == ['###', '#.#', '###', '#.#', '###']:
        return 8
    else:
        return 9

def main():
    N = int(readline())
    S = [readline().rstrip() for _ in range(5)]
    for p in range(N):
        start = 1 + 4 * p
        seg = [line[start:start+3] for line in S]
        print(check(seg), end='')

if __name__ == '__main__':
    main()