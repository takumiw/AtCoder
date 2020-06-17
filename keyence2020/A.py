import sys
readline = sys.stdin.readline

def main():
    H = int(readline())
    W = int(readline())
    N = int(readline())
    print(-(-N // max(H, W)))

if __name__ == '__main__':
    main()