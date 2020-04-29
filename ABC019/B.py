s = input()
pre = s[0]
cnt = 1
for i in range(1, len(s)):
    if s[i] == pre:
        cnt += 1
    else:
        print(s[i-1] + str(cnt), end='')
        pre = s[i]
        cnt = 1

print(s[-1] + str(cnt))