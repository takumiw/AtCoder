import sys
readline = sys.stdin.readline

def main():
    N = int(readline())
    stack = [int(readline())]

    for _ in range(N-1):
        w = int(readline())
        cand = [s for s in stack if s >= w]
        if not cand:
            stack.append(w)
        else:
            stack[stack.index(min(cand))] = w
    
    print(len(stack))

if __name__ == '__main__':
    main()