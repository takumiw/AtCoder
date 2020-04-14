from heapq import heapify, heappush, heappop
from operator import itemgetter

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    heapify(A)

    query = [list(map(int, input().split())) for _ in range(M)]
    query.sort(key=itemgetter(1), reverse=True)

    for b, c in query:
        for _ in range(b):
            m = heappop(A)
            if m >= c:
                heappush(A, m)
                break
            heappush(A, c)
        else:
            continue
        break
    
    print(sum(A))


if __name__ == "__main__":
    main()