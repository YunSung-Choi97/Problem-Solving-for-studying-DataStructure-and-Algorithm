def compress(target, length):  # target: 압축할 문자열, length: 압축 단위 길이
    result = ''  # 압축 결과
    pre_sub_str = target[:length]  # 이전에 선택된 부분 문자열
    count = 1  # 연속 등장 횟수
    idx = length  # 현재 위치
    while idx < len(target):
        # sub_str: 선택된 부분 문자열
        if idx + length < len(target):
            sub_str = target[idx:idx + length]
        else:
            sub_str = target[idx:]
        # 이전에 선택된 부분 문자열과 동일 여부에 따라 압축 진행
        if sub_str == pre_sub_str:
            count += 1
        else:
            if count == 1:
                result += pre_sub_str
            else:
                result += str(count) + pre_sub_str
            pre_sub_str = sub_str
            count = 1
        idx += length
    # 마지막 부분 처리
    if count == 1:
        result += pre_sub_str
    else:
        result += str(count) + pre_sub_str
    
    return result


def solution(s):
    answer = len(s)  # 압축되지 않는 경우 문자열 그대로 저장
    
    for length in range(1, len(s) // 2 + 1):
        result = compress(s, length)
        answer = min(answer, len(result))  # 가장 짧게 압축된 길이 채택

    # 결과 제출
    return answer

''' 입력 예시 1
aabbaccc
'''
''' 출력 예시 1
7
'''

''' 입력 예시 2
ababcdcdababcdcd
'''
''' 출력 예시 2
9
'''

''' 입력 예시 3
abcabcdede
'''
''' 출력 예시 3
8
'''

''' 입력 예시 4
abcabcabcabcdededededede
'''
''' 출력 예시 4
14
'''

''' 입력 예시 5
xababcdcdababcdcd
'''
''' 출력 예시 5
17
'''