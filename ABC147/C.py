import sys
N = int(sys.stdin.readline())

testimonies = [[-1 for _ in range(N)] for _ in range(N)]
for i in range(N):
    A = int(sys.stdin.readline())
    for _ in range(A):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        testimonies[i][x-1] = y

def check(honest_persons):
    flag = True
    for i in range(N):
        if honest_persons[i]:
            for j in range(N):
                if testimonies[i][j] == -1:
                    continue
                if testimonies[i][j] != honest_persons[j]:
                    flag = False
                    break
            else:
                continue
            break
    return flag

def main():
    ans = 0
    for i in range(1, 2**N):
        honest_persons = bin(i)[2:].zfill(N)
        honest_persons = list(map(int, list(honest_persons)))

        if check(honest_persons):
            ans = max(ans, sum(honest_persons))

    print(ans)

if __name__ == '__main__':
    main()