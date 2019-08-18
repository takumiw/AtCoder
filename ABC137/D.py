import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    jobs = {}
    for _ in range(N):
        A, B = map(int, input().split())
        if A > M:
            continue
        if A in jobs.keys():
            jobs[A] += [-B]
        else:
            jobs[A] = [-B]

    profit = 0
    days = jobs.keys()
    potential_jobs = []
    
    # M-1日後から今日まで遡る
    for elappsed_day in range(1, M+1):
        if elappsed_day in days:
            for job in jobs[elappsed_day]:
                heappush(potential_jobs, job)
        if len(potential_jobs) > 0:
            profit += heappop(potential_jobs)
            
    print(-profit)

if __name__ == "__main__":
    main()
