def main():
    S = list(map(int, list(input())))
    cnt1, cnt2 = 0, 0
    for i, s in enumerate(S):
        if i % 2 == 0:
            if s:
                cnt1 += 1
            else:
                cnt2 += 1
        else:
            if s:
                cnt2 += 1
            else:
                cnt1 += 1
    print(min(cnt1, cnt2))


if __name__ == '__main__':
    main()