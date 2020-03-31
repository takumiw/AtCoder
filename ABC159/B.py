def judge_kaibun(text):
    if len(text) % 2 == 0:
        if text[:len(text)//2] == text[len(text)//2:][::-1]:
            return True
        else:
            return False
    else:
        if text[:len(text)//2] == text[len(text)//2+1:][::-1]:
            return True
        else:
            return False


S = input()
if judge_kaibun(S) and judge_kaibun(S[:len(S)//2]) and judge_kaibun(S[len(S)//2+1:]):
    print('Yes')
else:
    print('No')