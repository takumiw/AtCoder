import sys
readline = sys.stdin.readline

def num2alpha(n):
    if n <= 26:
        return chr(64 + n)
    elif n % 26 == 0:
        return num2alpha(n // 26 - 1) + chr(90)
    else:
        return num2alpha(n // 26) + chr(64 + n % 26)

def main():
    N = int(readline())
    print(num2alpha(N).lower())

if __name__ == '__main__':
    main()