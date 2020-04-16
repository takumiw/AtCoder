from collections import deque
N = int(input())

def split_by_zero(l):
    if 0 not in l:
        return [l]
    ret_l = []
    while 0 in l:
        idx = l.index(0)
        if l[:idx]:
            ret_l.append(l[:idx])
        l = l[idx+1:]
    if l:
        ret_l.append(l)
    return ret_l

def main():
    
    H = list(map(int, input().split()))
    H = split_by_zero(H)
    que = deque(H)

    cnt = 0
    while que:
        q = que.popleft()
        q = [i-1 for i in q]
        cnt += 1
        q = split_by_zero(q)
        if q:
            for qq in q:
                que.append(qq)
    
    print(cnt)


if __name__ == "__main__":
    main()