import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    l0 = 2
    l1 = 1
    if N == 1:
        print(l1)
        return
    for i in range(2, N+1):
        li = l0 + l1
        l0 = l1
        l1 = li
    print(li)
    

if __name__ == '__main__':
    main()