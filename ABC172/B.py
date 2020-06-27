import sys
readline = sys.stdin.readline

def main():
    S = readline().rstrip()
    T = readline().rstrip()
    res = 0
    for s, t in zip(S, T):
        if s != t:
            res += 1
    
    print(res)

if __name__ == '__main__':
    main()