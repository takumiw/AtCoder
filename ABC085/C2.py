N, Y = map(int, input().split())

for n_10000 in range(min(N+1, Y//10000+1)):
    for n_5000 in range(min(N-n_10000+1, (Y-n_10000*10000)//5000+1)):
        n_1000 = N - n_10000 - n_5000
        if n_10000 * 10000 + n_5000 * 5000 + n_1000 * 1000 == Y:
            print(n_10000, n_5000, n_1000)
            exit()

print('-1 -1 -1')