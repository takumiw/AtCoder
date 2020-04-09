import math

def is_prime(x):
    if x < 2: return False  # 2未満に素数はない
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
    X = int(input())
    while 1:
        if is_prime(X):
            print(X)
            break
        X += 1


if __name__ == '__main__':
    main()