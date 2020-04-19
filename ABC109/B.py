import sys
readline = sys.stdin.readline

def main():
    n = int(readline())
    w1 = readline().rstrip()
    l = w1[-1]
    words = set()
    words.add(w1)
    for _ in range(n-1):
        w = readline().rstrip()
        if w[0] == l and w not in words:
            l = w[-1]
            words.add(w)
        else:
            print('No')
            return
    
    print('Yes')


if __name__ == '__main__':
    main()