import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    N = 1000 - N
    res = 0
    for m in [500, 100, 50, 10, 5, 1]:
        n = N // m
        res += n
        N -= m * n
   
   print(res)

if __name__ == "__main__":
    main()
