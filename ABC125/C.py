import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A = sorted(A)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    
    return divisors

def main():
    if len(A) <= 2:
        print(max(A))
        exit()
    else:
        all_divisors = list(set(make_divisors(A[0]) + make_divisors(A[1])))

    ans = 1
    for divisor in all_divisors:
        cnt = 0
        for a in A:
            if a % divisor != 0:
                cnt += 1
            if cnt == 2:
                break
        if cnt < 2:
            ans = max(ans, divisor)

    print(ans)

if __name__ == '__main__':
    main()