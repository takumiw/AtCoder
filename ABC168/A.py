import sys
readline = sys.stdin.readline

def main():
    N = readline().rstrip()
    if N[-1] in ['2', '4', '5', '7', '9']:
        print('hon')
    elif N[-1] in ['0', '1', '6', '8']:
        print('pon')
    else:
        print('bon')


if __name__ == '__main__':
    main()