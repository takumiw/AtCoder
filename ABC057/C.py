import sys
readline = sys.stdin.readline

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

def main():
    N = int(readline())
    divisors = make_divisors(N)
    le = len(divisors)
    if le % 2 == 1:
        print(len(str(divisors[le//2])))
    else:
        print(len(str(divisors[le//2])))

if __name__ == '__main__':
    main()