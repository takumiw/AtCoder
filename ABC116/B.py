s = int(input())

nums = {s}
while True:
    if s % 2 == 0:
        s //= 2
    else:
        s = 3 * s + 1
    if s in nums:
        break
    nums.add(s)

print(len(nums)+1)