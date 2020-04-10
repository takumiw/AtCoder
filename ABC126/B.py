S = input()
f, l = S[:2], S[2:]

if 1 <= int(f) <= 12 and 1 <= int(l) <= 12:
    print('AMBIGUOUS')
elif 1 <= int(f) <= 12:
    print('MMYY')
elif 1 <= int(l) <= 12:
    print('YYMM')
else:
    print('NA')