import sys
readline = sys.stdin.readline

def main():
    N, H = map(int, readline().rstrip().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, readline().rstrip().split())
        A.append(a)
        B.append(b)
    
    a_max = max(A)
    B.sort(reverse=True)
    damage = 0
    cost = 0
    for b in B:
        if b < a_max:
            break
        damage += b
        cost += 1
        if damage >= H:
            break
    if damage < H:
        cost += -(-(H - damage) // a_max)
    
    print(cost)
    return

if __name__ == '__main__':
    main()