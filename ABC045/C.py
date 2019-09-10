S = input()

# bit全探索で解く
def solve():
    ans = 0

    for i in range(2**(len(S)-1)):
        value = list(S)
        bit = list(str(bin(i))[2:].zfill(len(S)-1))
        for i, p in enumerate(bit):
            if int(p):
                value[i] = value[i] + '+'
        values = ''.join(value).split('+')
        values = list(map(int, values))
        ans += sum(values)
    print(ans)

if __name__ == "__main__":
    solve()