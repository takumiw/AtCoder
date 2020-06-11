import sys
readline = sys.stdin.readline

def main():
    N, M, Q = map(int, readline().rstrip().split())
    solved = [[] for _ in range(N)]  # 参加者iが解いた問題
    score = [N] * M  # 各問題のスコア
    for _ in range(Q):
        input_line = readline().rstrip().split()
        if len(input_line) == 2:
            _, n = map(int, input_line)
            res = sum([score[pro] for pro in solved[n-1]])
            print(res)
        else:
            _, n, m = map(int, input_line)
            score[m-1] -= 1
            solved[n-1].append(m-1)

if __name__ == '__main__':
    main()