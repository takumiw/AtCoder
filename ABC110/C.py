import sys
sys.setrecursionlimit(10 ** 6)

def main():
    S = input()
    T = input()
    pair1 = {}
    pair2 = {}
    for i in range(len(S)):
        if S[i] not in pair1.keys():
            pair1[S[i]] = T[i]
        else:
            if pair1[S[i]] != T[i]:
                print('No')
                return
        if T[i] not in pair2.keys():
            pair2[T[i]] = S[i]
        else:
            if pair2[T[i]] != S[i]:
                print('No')
                return
        
    print('Yes')


if __name__ == '__main__':
    main()