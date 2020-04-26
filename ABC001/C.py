import sys
readline = sys.stdin.readline
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

def main():
    Deg, Dis = map(int, readline().rstrip().split())
    az = [
        'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 
        'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    if Deg/10 < 11.25 or Deg/10 >= 348.75:
        a = 'N'
    else:
        a = az[int(((Deg / 10) // 11.25 - 1) // 2)]
    
    ws = Dis / 60
    ws = Decimal(str(ws)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
    ws = float(ws)
    if ws <= 0.2:    wp = 0
    elif ws <= 1.5:  wp = 1
    elif ws <= 3.3:  wp = 2
    elif ws <= 5.4:  wp = 3
    elif ws <= 7.9:  wp = 4
    elif ws <= 10.7:  wp = 5
    elif ws <= 13.8:  wp = 6
    elif ws <= 17.1:  wp = 7
    elif ws <= 20.7:  wp = 8
    elif ws <= 24.4:  wp = 9
    elif ws <= 28.4:  wp = 10
    elif ws <= 32.6:  wp = 11
    else:  wp = 12

    if wp == 0:
        a = 'C'

    print(a, wp)
    

if __name__ == '__main__':
    main()