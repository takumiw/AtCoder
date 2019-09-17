from itertools import permutations

numbers = list(map(int, list(input())))

def solve():
    '''bit全探索で解く'''
    candidates = []
    for i in range(2**3):
        
        candidates.append(bin(i)[2:].zfill(3))
    
    for candidate in candidates:
        s = numbers[0]
        for i, c in enumerate(list(candidate)):
            if c == '1':
                s += numbers[i+1]
            else:
                s -= numbers[i+1]
        if s == 7:
            candidate = ''.join(candidate)
            candidate = candidate.replace('1', '+')
            candidate = candidate.replace('0', '-')
            for i in range(3):
                print(numbers[i], end='')
                print(candidate[i], end='')
                
            print(numbers[-1], end='')
            print('=7') 
            return

if __name__ == '__main__':
    solve()