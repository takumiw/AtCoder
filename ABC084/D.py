import sys
readline = sys.stdin.readline
import math
    
def is_prime(x):
    if x < 2: return False
    if x == 2 or x == 3 or x == 5: return True  # 2,3,5は素数
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0: return False  # 2,3,5の倍数は合成数
    prime = 7
    step = 4
    while prime <= math.sqrt(x):
        if x % prime == 0: return False
        prime += step
        step = 6 - step
    return True

def main():
    Q = int(readline())
    is_2017 = [True] * (10**5 // 2)
    for i in range(10**5//2):
        if not is_prime(2*i+1):
            is_2017[i] = False
        if not is_prime(i+1):
            is_2017[i] = False

    is_2017[0] = 0
    for i in range(1, 10**5//2):
        is_2017[i] += is_2017[i-1]
    
    for _ in range(Q):
        l, r = map(int, readline().rstrip().split())
        if l == 1:
            print(is_2017[(r-1)//2])
        else:
            print(is_2017[(r-1)//2] - is_2017[(l-1)//2-1])


if __name__ == '__main__':
    main()