from collections import deque

def main():
    S = input()
    Q = int(input())

    S = deque(list(S))
    rev = 1  # 正方向: 1, 逆方向: -1
    for _ in range(Q):
        input_line = input().split()
        #print('query', input_line)
        if len(input_line) == 1:
            rev *= -1
        else:
            _, f, c = input_line
            if f == '1':
                if rev == 1:
                    S.appendleft(c)
                else:
                    S.append(c)
            else:
                if rev == 1:
                    S.append(c)
                else:
                    S.appendleft(c)
        #print(rev)
        #print(S)
        #print()

    # print(S)
    if rev == 1:
        print(''.join(S))
    else:
        print(''.join(list(S)[::-1]))


if __name__ == '__main__':
    main()