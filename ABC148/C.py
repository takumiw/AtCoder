import fractions

A, B = map(int, input().split())

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

def solve():
    print(lcm(A, B))

if __name__ == '__main__':
    solve()