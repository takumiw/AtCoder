import re
N = int(input())
S = input()
COLORS = list(set(list(S)))

for color in COLORS:
    S = re.sub('{}+'.format(color), color, S)

print(len(S))