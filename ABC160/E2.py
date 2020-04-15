from heapq import heapify, heappush, heappop

def main():
    X, Y, A, B, C = map(int, input().split())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    R = list(map(int, input().split()))

    P.sort(reverse=True)
    Q.sort(reverse=True)
    PQR = P[:X] + Q[:Y] + R
    PQR.sort(reverse=True)    
    print(sum(PQR[:X+Y]))
    

if __name__ == "__main__":
    main()