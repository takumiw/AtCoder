import sys
readline = sys.stdin.readline

def main():
    s = readline().rstrip()
    t = readline().rstrip()
    if s == t:
        print('same')
    elif s.lower() == t.lower():
        print('case-insensitive')
    else:
        print('different')


if __name__ == '__main__':
    main()