import sys
readline = sys.stdin.readline
from heapq import heapify, heappush, heappop

def main():
    N, M = map(int, readline().rstrip().split())
    inp = [list(map(int, readline().rstrip().split())) for _ in range(M)]
    pref = {}
    for p, y in inp:
        pref.setdefault(p, [])
        pref[p].append(y)

    pref_year_id = {}
    for p, years in pref.items():
        heapify(years)
        p_id = str(p).zfill(6)
        pref_year_id[p] = {}
        for i in range(1, len(years)+1):
            year = heappop((years))
            pref_year_id[p][year] = p_id + str(i).zfill(6)
    
    for p, y in inp:
        print(pref_year_id[p][y])

if __name__ == '__main__':
    main()