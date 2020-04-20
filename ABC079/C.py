import sys
readline = sys.stdin.readline

def main():
    num = list(readline())
    op = ['+', '-']
    for op1 in op:
        for op2 in op:
            for op3 in op:
                f = num[0] + op1 + num[1] + op2 + num[2] + op3 + num[3]
                if eval(f) == 7:
                    print(f + '=7')
                    return


if __name__ == '__main__':
    main()