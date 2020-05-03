import sys
readline = sys.stdin.readline

def main():
    D, G = map(int, readline().rstrip().split())
    G //= 100
    PC = [tuple(map(int, readline().rstrip().split())) for _ in range(D)]
    ans = 10 ** 4
    for i in range(2**D):
        b = bin(i)[2:].zfill(D)
        score = 0
        cost = 0
        for i, e in enumerate(b):
            if e == '1':
                score += PC[i][0] * (i+1) + PC[i][1] // 100
                cost += PC[i][0]
        
        if '0' in b:
            m = D - b[::-1].index('0') - 1
            for _ in range(PC[m][0]-1):
                if score >= G:
                    break
                score += m + 1
                cost += 1
        
        if score >= G:
            ans = min(ans, cost)
    
    print(ans)

if __name__ == '__main__':
    main()