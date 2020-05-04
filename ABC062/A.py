x, y = map(int, input().split())
if x in [4,6,9,11] and y in [4,6,9,11]:
    ans = 'Yes'
elif x in [1,3,5,7,8,10,12] and y in [1,3,5,7,8,10,12]:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)