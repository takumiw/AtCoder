import math
N, K = map(int, input().split())

print(math.floor(math.log(N) / math.log(K)) + 1)