import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jobs = [list(map(int, input().rstrip().split())) for _ in range(N)]

