import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    S = [int(readline()) for _ in range(N)]
    m = sum(S)
    if m % 10 != 0:
        print(m)
    else:
        mi = [s for s in S if s % 10 != 0]
        if len(mi):
            print(m - min(mi))
        else:
            print(0)
    

if __name__ == '__main__':
    main()