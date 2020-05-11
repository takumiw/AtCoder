import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A, B, C, D, E = [int(readline()) for _ in range(5)]
    res = -(-N // min(A, B, C, D, E)) + 4
    print(res)

if __name__ == '__main__':
    main()