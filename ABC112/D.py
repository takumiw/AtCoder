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
    N, M = map(int, readline().rstrip().split())
    ans = 1
    for d in  make_divisors(M):
        if M // d >= N:
            ans = d
        else:
            break

    print(ans)

if __name__ == '__main__':
    main()