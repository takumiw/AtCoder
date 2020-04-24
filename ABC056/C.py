import sys
readline = sys.stdin.readline

def main():
    X = int(readline())
    x2 = 2 * X
    for i in range(1, X+1):
        if i * (i + 1) >= x2:
            print(i)
            return

    
if __name__ == '__main__':
    main()