import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = [set(readline().rstrip()) for _ in range(N)]
    res = ''
    for i in range(N//2):
        mul = A[i] & A[-i-1]
        if len(mul) == 0:
            print(-1)
            return
        res += list(mul)[0]
    
    if N % 2 == 0:
        print(res + res[::-1])
    else:
        print(res + list(A[N//2])[0] + res[::-1])


if __name__ == '__main__':
    main()