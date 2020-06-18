import sys
readline = sys.stdin.readline

def main():
    W, H = map(int, readline().rstrip().split())
    W = 2 * W - 1
    amd = [readline().rstrip() for _ in range(H)]
    goal = readline().rstrip()

    idx = goal.index('o')
    for line in amd[::-1]:
        if idx > 0 and line[idx-1] == '-':
            idx -= 2
        elif idx < W - 1:
            if line[idx+1] == '-':
                idx += 2
    
    print(idx // 2 + 1)

if __name__ == '__main__':
    main()