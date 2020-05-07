import sys
readline = sys.stdin.readline

def main():
    S = readline().rstrip()
    T = S.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
    if not T:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()