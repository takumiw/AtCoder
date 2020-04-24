s = list(input())
ss = s[::-1]
print((len(s) - ss.index('Z')) - s.index('A'))