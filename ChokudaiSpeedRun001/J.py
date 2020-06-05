import sys
readline = sys.stdin.readline

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n+1)
 
    def __iter__(self):
        psum = 0
        for i in range(self.size):
            csum = self.sum(i+1)
            yield csum - psum
            psum = csum
        raise StopIteration()
 
    def __str__(self):  # O(nlogn)
        return str(list(self))
 
    def sum(self, i):
        # [0, i) の要素の総和を返す
        if not (0 <= i <= self.size): raise ValueError("error!")
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
 
    def __getitem__(self, key):
        if not (0 <= key < self.size): raise IndexError("error!")
        return self.sum(key+1) - self.sum(key)
 
    def __setitem__(self, key, value):
        # 足し算と引き算にはaddを使うべき
        if not (0 <= key < self.size): raise IndexError("error!")
        self.add(key, value - self[key])

def main():
    N = int(readline())
    A = list(map(int, readline().rstrip().split()))

    bit = Bit(max(A) + 1)
    res = 0
    
    for i, a in enumerate(A):
        res += i - bit.sum(a+1)
        bit.add(a, 1)
    
    print(res)

if __name__ == '__main__':
    main()