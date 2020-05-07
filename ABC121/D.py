import sys
readline = sys.stdin.readline

def f(x):
    if x % 2 == 0:
        if (x//2) % 2 == 0:
            return x ^ 0
        else:
            return x ^ 1
    else:
        if ((x+1)//2) % 2 == 0:
            return 0
        else:
            return 1

def main():
    A, B = map(int, readline().rstrip().split())
    print(f(A-1) ^ f(B))

if __name__ == '__main__':
    main()