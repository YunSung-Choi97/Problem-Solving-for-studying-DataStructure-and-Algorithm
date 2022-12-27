n = int(input())  # 캐릭터의 점수

score = list(map(int, str(n)))  # 점수의 각 자리를 리스트로 저장
left_score, right_score = 0, 0  # 왼쪽 부분의 각 자릿수의 합, 오른쪽 부분의 각 자릿수의 합
for i in range(len(score) // 2):
    left_score += score[i]
    right_score += score[i + len(score) // 2]

# 결과 출력
if left_score == right_score:
    print('LUCKY')
else:
    print('READY')

''' 입력 예시 1
123402
'''
''' 출력 예시 1
LUCKY
'''

''' 입력 예시 2
7755
'''
''' 출력 예시 2
READY
'''