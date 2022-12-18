from collections import deque

s = deque(map(int, input()))  # 입력받은 숫자정보

no_duplicate = [s.popleft()]  # 숫자정보에서 연속된 동일한 수들을 하나로 만듬
while s:
    now = s.popleft()
    
    if now != no_duplicate[-1]:
        no_duplicate.append(now)

print(len(no_duplicate) // 2)  # 결과 출력

''' 입력 예시 1
0001100
'''
''' 출력 예시 1
1
'''