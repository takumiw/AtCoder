import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().rstrip().split()))

for i in range(N-1):
    if H[i] > H[i+1]:
        print('No')
        sys.exit() 
    H[i+1] = max(H[i], H[i+1]-1)
            
print('Yes')