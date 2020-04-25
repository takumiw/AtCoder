# (a ** n) % mod
def modinv(n, a, mod=MOD):
    return pow(a, n, mod)

# nCr % mod
def comb(n, r, mod=MOD):
    res = 1
    fac = 1
    for i in range(r):
        res *= n-i
        res %= mod
        fac *= i+1
        fac %= mod
    return res * pow(fac, mod-2, mod) % mod

### N! % mod
def factorial(N, mod=MOD):
    res = 1
    for i in range(2, N+1):
        res *= i
        res %= mod
    return res


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


### 重複を含む順列を生成する l=[1, 2], n=3 -> [[1,1,1],[1,1,2],[1,1,3],...]
from itertools import product
def pro(l, n):
    return list(product(l, repeat=n))


# 重複を含む順列を生成する
from itertools import permutations
def permutation(l, n):
    '''
    lPnの順列を生成する
    @param l: 順列を生成する要素のリスト
    @param n: lからいくつ取り出すか
    @return list: 全ての順列
    '''
    return [p for p in permutations(l, n)]


# 組み合わせを生成する
from itertools import combinations
def combination(l, n):
    '''
    lCnの組み合わせを生成する
    @param l: 組み合わせを生成する要素のリスト
    @param n: lからいくつ取り出すか
    @return list: 全ての組み合わせ
    '''
    return [p for p in combinations(l, n)]


# 2以上の整数の約数を列挙する, O(√n)
def make_divisors(n) -> list:
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


### N進数->10進数
def base_n_to_10(s, n):
    return int(s, n)

### 10進数->N進数
def base_10_to_n(i, n):
    if i//n:
        return base_10_to_n(i//n, n) + str(i % n)
    return str(i % n)

### 行列を標準出力する
def print_matrix(matrix):
    h = len(matrix[0])
    w = len(matrix[1])
    yticks = [str(i) for i in range(w)]
    print('  | ' + ' '.join(yticks))
    print('--' * (w + 2))
    for i, l in enumerate(matrix):
        print('{} | '.format(i), end='')
        print(' '.join(list(map(str, l))))

### 最大公約数を求める
import math
def gcd(a, b):
    return math.gcd(a, b)

def gcd(a, b, c):
    return math.gcd(math.gcd(a, b), c)

### 最小公倍数を求める
import math
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(a, b, c):
    return lcm_base(lcm_base(a, b), c)

### ある非負整数nに含まれる素因数dの数
def count_factor(n, d=2):
    if n % d != 0:
        return 0
    for i in range(n):
        if n & d<<i:
            return i + 1

### UnionFind
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())