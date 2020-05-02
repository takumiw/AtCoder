import sys
readline = sys.stdin.readline

def main():
    K = int(readline())
    A, B = map(int, readline().rstrip().split())
    for i in range(A, B+1):
        if i % K == 0:
            print('OK')
            exit()
    
    print('NG')


if __name__ == '__main__':
    main()