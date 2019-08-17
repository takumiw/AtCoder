import sys 
from collections import Counter

def main():
  input = sys.stdin.readline
  N = int(input())
  texts = [''.join(sorted(list(input().rstrip()))) for _ in range(N)]
  c = Counter(texts)
  cnt = 0
  for t in c.values():
    if t > 1:
      cnt += (t * (t-1)) // 2
  print(cnt)
 
if __name__ == '__main__':
  main()
