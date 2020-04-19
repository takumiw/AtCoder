a, b, c = map(int, input().split())
print(min(
    abs(a-b) + abs(b-c),
    abs(a-c) + abs(c-b),
    abs(b-a) + abs(a-c),
    abs(b-c) + abs(c-a),
    abs(c-a) + abs(a-b),
    abs(c-b) + abs(b-a)
))