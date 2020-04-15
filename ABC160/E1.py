from heapq import heapify, heappush, heappop

def main():
    X, Y, A, B, C = map(int, input().split())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    R = list(map(int, input().split()))

    P.sort(reverse=True)
    Q.sort(reverse=True)
    R.sort(reverse=True)
    PQ = P[:X] + Q[:Y]
    heapify(PQ)

    while R:
        mpq = heappop(PQ)
        mr = R.pop(0)
        if mpq >= mr:
            heappush(PQ, mpq)
            break
        heappush(PQ, mr)
    
    print(sum(PQ))
    

if __name__ == "__main__":
    main()