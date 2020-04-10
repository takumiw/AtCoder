from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))

    c = Counter(A)
    vals = c.keys()
    cnts = c.values()

    subs = {}
    a_sum = 0
    for v, c in zip(vals, cnts):
        subs[v] = c - 1
        a_sum += (c * (c-1)) // 2
    
    for a in A:
        print(a_sum - subs[a])


if __name__ == '__main__':
    main()