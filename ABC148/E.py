def main():
    N = int(input())

    if N % 2 == 1:
        print(0)
        exit()
    
    ans = 0
    d = 10
    while d <= N:
        ans += (N // d)
        d *= 5
    
    print(ans)


if __name__ == "__main__":
    main()