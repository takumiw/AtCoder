### 逆元シリーズ
# (a ** n) % mod
def modinv(n, a, mod=MOD):
    return pow(a, n, mod)

# nCr % mod O(r)
def comb(n, r, mod=MOD):
    r = min(n - r, r)
    res = 1
    fac = 1
    for i in range(r):
        res *= n - i
        res %= mod
        fac *= i + 1
        fac %= mod
    return res * pow(fac, mod-2, mod) % mod

# nCr % mod 前処理にO(n), 毎回の呼び出しにO(1)
fact = [1] * (N+1)
finv = [1] * (N+1)
inv = [1] * (N+1)
inv[0] = 0
for i in range(2, N+1):
    fact[i] = (fact[i-1] * i % MOD)
    inv[i] = (-inv[MOD%i] * (MOD // i)) % MOD
    finv[i] = (finv[i-1] * inv[i]) % MOD

def comb(n, r, mod=MOD):
    if r < 0 or n < r:
        return 0
    return fact[n] * finv[r] * finv[n-r] % mod


### N! % mod
def factorial(N, mod=MOD):
    res = 1
    for i in range(2, N+1):
        res *= i
        res %= mod
    return res


### 優先度付きキュー
from heapq import heapify, heappush, heappop
def solve_heapq(l):
    heapify(l)  # リストlをheapqにする
    m = heappop(l)  # heapqの最小値をpopする O(1)
    heappush(l, 3)  # heapqに値(3)を追加する O(logN)


### 二分探索, リストlにxがあるか否か O(logn)
from bisect import bisect_left
def binary_search(l, x):
    '''
    @param l: 二分探索する昇順ソート済みリスト
    @param x: 二分探索する値
    @return bool: リストにxが存在するか否か
    '''
    i = bisect_left(l, x)
    if i != len(l) and l[i] == x:
        return True
    return False


### 順列/組み合わせシリーズ
# 重複を含む順列を生成する l=[1,2], n=3 -> [[1,1,1],[1,1,2],[1,1,3],...]
from itertools import product
def pro(l, n):
    return list(product(l, repeat=n))

# 重複を含まない順列を生成する l=[1,2,3], n=3 -> [[1,2,3],[1,3,2],[2,1,3],...]
from itertools import permutations
def permutation(l, n):
    return list(permutations(l, n))

# 重複を含む組み合わせを生成する l=[1,2,3], n=3 -> [[1,1,1],[1,1,2],[1,1,3],[1,2,2]...]
from itertools import combinations_with_replacement
def combination(l, n):
    return list(combinations_with_replacement(l, n))

# 重複を含まない組み合わせを生成する l=[1,2,3], n=2 -> [[1,2],[1,3],[2,3]]
from itertools import combinations
def combination(l, n):
    return list(combinations(l, n))


### 約数/素数シリーズ
# 2以上の整数の約数を列挙する, O(√n)
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()  # 必要に応じてソートする(O(nlogn))
    return divisors

# 素因数分解 factorize(900) -> [2, 2, 3, 3, 5, 5]
def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

##素因数分解 factorize(900) -> [(2, 2), (3, 2), (5, 2)]
def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

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


### N進数->10進数 (n進数の文字列s)
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

### 四捨五入する, r=0: 整数に四捨五入, 0.1: 小数点第一桁に四捨五入, etc.
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
def round(f, r=0):
    return Decimal(str(f)).quantize(Decimal(str(r)), rounding=ROUND_HALF_UP)

### decimal型, デフォルトでは28桁まで浮動小数点を扱える
from decimal import Decimal
def to_decimal(n: str):
    return Decimal(n)

### 切り上げする, a / b
def ceil(a, b):
    return -(-a//b)

### 最大二部マッチング
# -> ABC091/C_networkx.py

### 配列の部分和をDPで求める
# -> ABC044/C.py

### グラフ系
# Warshall Floyd ->  ABC022/C.py, ABC012/D, ABC079/D, ARC035/C

# Dijkstra
from scipy.sparse.csgraph import dijkstra
G = dijkstra(path, indices=0)  # 空間計算量: O(N^2)
from heapq import heapify, heappush, heappop
def dijkstra(path, N, start):
    """
    Args:
        path (list): [[(cost, node), (cost, node), ...], [], [], ...]
    """
    visited = [False] * N
    que = [(0, start)]
    heapify(que)  # 始点aから各頂点への(距離, 頂点ID)
    dist = [-1] * N  # 始点aから各頂点への距離
    dist[start] = 0  # 始点aからaへの距離は0
    while que:
        d, v = heappop(que)  # 始点から最短距離の頂点を(確定ノード)を取り出す
        visited[v] = True  # 確定フラグを立てる
        # 接続先ノードの情報を更新する
        for d, to in path[v]:
            cost = dist[v] + d
            if dist[to] < 0 or cost < dist[to]:
                dist[to] = cost
                if not visited[to]:
                    heappush(que, (cost, to))

    return dist

# Bellman-Ford -> ABC061/D

# DFS/BFS -> ABC036/D, ABC054/C

### UnionFind (https://note.nkmk.me/python-union-find/)
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