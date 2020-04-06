from collections import deque

def main():
    K = int(input())
    que = deque([i for i in range(1, 10)])

    while K:
        if K == 1:
            ans = que.popleft()
            break
        K -= 1
        v = que.popleft()
        if v % 10 == 0:
            que.append(v * 10)
            que.append(v * 10 + 1)
        elif v % 10 == 9:
            que.append(v * 10 + 8)
            que.append(v * 10 + 9)
        else:
            que.append(v * 10 + (v % 10 - 1))
            que.append(v * 10 + (v % 10))
            que.append(v * 10 + (v % 10 + 1))
    print(ans)

if __name__ == '__main__':
    main()