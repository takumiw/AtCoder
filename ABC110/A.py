import sys

abc = list(map(int, sys.stdin.readline().rstrip().split()))
abc.sort(reverse=True)
print(int(str(abc[0])+str(abc[1])) + abc[2])