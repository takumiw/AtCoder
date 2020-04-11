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


def main():
    N, M, K = map(int, input().split())
    num_friends = [0 for _ in range(N)]
    blocks = [[] for _ in range(N)]
    uf = UnionFind(N)

    for _ in range(M):
        a, b = map(int, input().split())
        num_friends[a-1] += 1
        num_friends[b-1] += 1
        uf.union(a-1, b-1)
    for _ in range(K):
        a, b = map(int, input().split())
        blocks[a-1].append(b-1)
        blocks[b-1].append(a-1)

    ans = []
    for i in range(N):
        cnt = uf.size(i) - 1 - num_friends[i]
        for j in blocks[i]:
            if uf.same(i, j):
                cnt -= 1
        ans.append(cnt)
    
    print(*ans)

if __name__ == "__main__":
    main()