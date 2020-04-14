def main():
    S = list(map(int, list(input())))

    cnt1 = sum(S)
    cnt0 = len(S) - cnt1
    print(2 * min(cnt0, cnt1))


if __name__ == "__main__":
    main()