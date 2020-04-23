import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    A = [0] + list(map(int, readline().rstrip().split())) + [0]
    s = sum([abs(A[i]-A[i-1]) for i in range(1, N+2)])
    for i in range(1, N+1):
        print(s + abs(A[i+1] - A[i-1]) - (abs(A[i+1]-A[i]) + abs(A[i]-A[i-1])))
    

if __name__ == '__main__':
    main()