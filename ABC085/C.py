N, Y = map(int, input().split())

def main():
    for num_10000 in range(N+1):
        for num_5000 in range(N+1-num_10000):
            num_1000 = N - num_10000 - num_5000
            if num_10000*10000 + num_5000*5000 + num_1000*1000 == Y:
                print(num_10000, num_5000, num_1000)
                return
    print('-1 -1 -1')

if __name__ == "__main__":
    main()