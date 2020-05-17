import sys
readline = sys.stdin.readline
import math

def main():
    A, B, H, M = map(int, readline().rstrip().split())
    rad_b = M / 60 * 360
    rad_a = H / 12 * 360 + 30 * (M / 60)
    rad_diff = min(rad_a - rad_b, 360 - (rad_a - rad_b))
    res = A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(rad_diff))
    print(math.sqrt(res))


if __name__ == '__main__':
    main()