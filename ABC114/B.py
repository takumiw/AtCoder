S = input()
res = 753
for i in range(len(S)-2):
    res = min(res, abs(int(S[i:i+3]) - 753))

print(res)