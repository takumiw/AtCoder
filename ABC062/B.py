import sys
readline = sys.stdin.readline

def main():
    H, W = map(int, readline().rstrip().split())
    ans = [['#']*(W+2)] + [['#']+readline().rstrip().split()+['#'] for _ in range(H)] + [['#']*(W+2)]
    ans = [''.join(l) for l in ans]
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()