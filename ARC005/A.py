import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    W = readline().rstrip()[:-1].split()
    res = len([1 for w in W if w == 'TAKAHASHIKUN' or w == 'Takahashikun' or w == 'takahashikun'])
    print(res)

if __name__ == '__main__':
    main()