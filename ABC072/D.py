import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    P = list(map(int, readline().rstrip().split()))
    l = ['x' if p == i+1 else 'o' for i, p in enumerate(P)]
    l = ''.join(l)
    ll = l.replace('xx', '')
    ans = (len(l) - len(ll)) // 2 + ll.count('x')
    print(ans)
    
if __name__ == '__main__':
    main()