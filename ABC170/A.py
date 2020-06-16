import sys
readline = sys.stdin.readline

def main():
    X = list(map(int, readline().rstrip().split()))
    for i, x in enumerate(X):
        if x != i + 1:
            print(i + 1)

if __name__ == '__main__':
    main()