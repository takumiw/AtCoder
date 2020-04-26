import sys
readline = sys.stdin.readline
MOD = 5

def main():
    N = int(readline())
    N %= 30
    l = [1, 2, 3, 4, 5, 6]
    for i in range(N):
        a1 = i % MOD
        a2 = i % MOD + 1
        e = l[a1]
        l[a1] = l[a2]
        l[a2] = e
    
    print(*l, sep='')
    

if __name__ == '__main__':
    main()