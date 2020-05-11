import sys
readline = sys.stdin.readline

N = int(readline())

def dfs(num):
    if int(num) > N:
        return 0
    if all(num.count(n) > 0 for n in '753'):
        res = 1
    else:
        res = 0
    for n in '753':
        res += dfs(num + n)
        
    return res


def main():
    print(dfs('0'))

if __name__ == '__main__':
    main()