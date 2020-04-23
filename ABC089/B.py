N = int(input())
S = input().split()
if len(set(S)) == 4:
    print('Four')
elif len(set(S)) == 3:
    print('Three')