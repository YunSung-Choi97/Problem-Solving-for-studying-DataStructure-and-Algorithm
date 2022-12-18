s = list(map(int, input()))  # 입력된 숫자정보

def calc():
    # S의 길이가 1인 경우
    if len(s) == 1:
        return s[0]
    result = s[0]
    # S의 첫 숫자가 0인 경우
    if s[0] == 0:
        result = s[1]
        for i in range(2, len(s)):
            if s[i] in [0, 1]:
                result += s[i]
            else:
                result *= s[i]
        return result
    # 그 외 경우
    for i in range(1, len(s)):
        if s[i] in [0, 1]:
            result += s[i]
        else:
            result *= s[i]
    return result

print(calc())  # 결과 출력

''' 입력 예시 1
02984
'''
''' 출력 예시 1
567
'''

''' 입력 예시 2
567
'''
''' 출력 예시 2
210
'''