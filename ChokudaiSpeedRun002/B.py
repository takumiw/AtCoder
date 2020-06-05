import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    for _ in range(N):
        a, b = map(int, readline().rstrip().split())
        print(a % b)

if __name__ == '__main__':
    main()