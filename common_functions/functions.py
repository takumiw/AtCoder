# (a ** n) % mod
def modinv(n, a, mod):
    return pow(a, n, mod)


# nCr % mod
def comb(n, r, mod):
    res = 1
    fac = 1
    for i in range(r):
        res *= n-i
        res %= mod
        fac *= i+1
        fac %= mod
    return res * pow(fac, mod-2, mod) % mod


from heapq import heapify, heappush, heappop
def solve_heapq(l: list):
    heapify(l)  # リストlをheapqにする
    m = heappop(l)  # heapqの最小値をpopする
    heappush(l, 3)  # heapqに値(3)を追加する


from bisect import bisect_left
def binary_search(l: list, x: int) -> bool:
    '''
    リストからxを探索する, O(logn)
    @param l: 二分探索する昇順ソート済みリスト
    @param x: 二分探索する値
    @return bool: リストにxが存在するか否か
    '''
    i = bisect_left(l, x)
    if i != len(l) and l[i] == x:
        return True
    return False


# 重複を含む順列を生成する
from itertools import permutations
def permutation(l: list, n: int) -> list:
    '''
    lPnの順列を生成する
    @param l: 順列を生成する要素のリスト
    @param n: lからいくつ取り出すか
    @return list: 全ての順列
    '''
    return [p for p in permutations(l, n)]


# 重複を含まない組み合わせを生成する
from itertools import combinations
def combination(l: list, n: int) -> list:
    '''
    lCnの組み合わせを生成する
    @param l: 組み合わせを生成する要素のリスト
    @param n: lからいくつ取り出すか
    @return list: 全ての組み合わせ
    '''
    return [p for p in combinations(l, n)]


# 2以上の整数の約数を列挙する, O(√n)
def make_divisors(n: int) -> list:
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()  # 必要に応じてソートする(O(nlogn))
    return divisors


# 素数かどうか判定する, O(√n)
import math
def is_prime(x: int) -> bool:
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