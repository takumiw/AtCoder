import sys
readline = sys.stdin.readline
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    N = int(readline())
    start = 1  # 各範囲でのスタートの値s
    cnt = 1  # 文字数
    while True:
        last = start * 26
        if start <= N <= last:
            break
        start = last + 1
        cnt += 1
    
    idx = N - start  # その文字数の中で何番目か (0番目スタート)

    res = ""
    while cnt:
        chara = idx // 26 ** (cnt - 1)
        idx -= 26 ** (cnt - 1) * chara
        chara = alp[chara]
        res += chara
        cnt -= 1
    
    print(res)


if __name__ == '__main__':
    main()