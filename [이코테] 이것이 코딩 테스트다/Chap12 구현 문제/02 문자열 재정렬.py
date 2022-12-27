s = input()  # 문자열

data = list(map(str, s))  # 문자열을 한 글자씩 분리해 리스트로 저장

string = []  # 문자열 중 알파벳 대문자만을 저장
sum_of_num = 0
for char in data:
    if ord('A') <= ord(char) <= ord('Z'):
        string.append(char)
    else:
        sum_of_num += int(char)
string.sort()  # 오름차순 정렬

# 결과 출력
print(''.join(string), sum_of_num, sep='')


''' 입력 예시 1
K1KA5CB7
'''
''' 출력 예시 1
ABCKK13
'''

''' 입력 예시 2
AJKDLSI412K4JSJ9D
'''
''' 출력 예시 2
ADDIJJJKKLSS20
'''