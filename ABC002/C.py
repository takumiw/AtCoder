xa, ya, xb, yb, xc, yc = map(int, input().split())
xb -= xa
xc -= xa
yb -= ya
yc -= ya

print(abs(yc*xb - xc*yb) / 2)