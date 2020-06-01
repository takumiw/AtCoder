import sys
readline = sys.stdin.readline
from decimal import Decimal
from math import floor

def main():
    A, B = readline().rstrip().split()
    print(floor(Decimal(A) * Decimal(B)))

if __name__ == '__main__':
    main()