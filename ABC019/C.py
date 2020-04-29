import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))
    cnt = set()
    for a in A:
        while a % 2 == 0:
            a //= 2
        cnt.add(a)
    
    print(len(cnt))


if __name__ == '__main__':
    main()