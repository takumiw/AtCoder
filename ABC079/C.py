numbers = list(input())
pm = ['+', '-']

for op1 in pm:
    for op2 in pm:
        for op3 in pm:
            s = numbers[0]+op1+numbers[1]+op2+numbers[2]+op3+numbers[3]
            if eval(s) == 7:
                print('{}=7'.format(s))
                exit()