inp = [int(input()) for _ in range(5)]
k = int(input())

if inp[-1] - inp[0] > k:
    print(':(')
else:
    print('Yay!')