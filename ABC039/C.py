S = input()
S  = S[:12]
o = 'WBWBWWBWBWBW'
l = ['Do', 'Si', 'La', 'La', 'So', 'So', 'Fa', 'Fa', 'Mi', 'Re', 'Re', 'Do']
for i in range(len(S)):
    s = S[i:] + S[:i]
    if s[:12] == o:
        print(l[i])
        break