import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    res = 0
    s = set()
    for _ in range(N):
        a, b = map(int, readline().rstrip().split())
        if (a, b) not in s and (b, a) not in s:
            s.add((a, b))
    
    print(len(s))

if __name__ == '__main__':
    main()