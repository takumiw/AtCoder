N, M = map(int, input().split())

def main():
    sub = [0] * N
    pen = [0] * N
    for _ in range(M):
        p, s = input().split()
        if s == 'AC':
            sub[int(p)-1] += 1
        else:
            if sub[int(p)-1] == 0:
                pen[int(p)-1] += 1


    ac = len([s for s in sub if s > 0])
    pen = sum([p for i, p in enumerate(pen) if sub[i] > 0])
    print(ac, pen)

if __name__ == '__main__':
    main()