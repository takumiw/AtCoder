import sys
readline = sys.stdin.readline

def main():
    sx, sy, tx, ty = map(int, readline().rstrip().split())
    r1 = 'U' * (ty-sy) + 'R' * (tx-sx)
    r2 = 'D' * (ty-sy) + 'L' * (tx-sx)
    r3 = 'L' + 'U' * (ty-sy+1) + 'R' * (tx-sx+1) + 'D'
    r4 = 'R' + 'D' * (ty-sy+1) + 'L' * (tx-sx+1) + 'U'
    print(r1 + r2 + r3 + r4)

if __name__ == '__main__':
    main()