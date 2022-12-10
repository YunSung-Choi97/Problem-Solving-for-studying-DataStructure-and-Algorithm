n = int(input())

# 시, 분, 초에 3이 포함되어 있는지 확인
count = 0
for hh in range(n + 1):
    if '3' in str(hh):
        count += 3600
        continue
    for mm in range(60):
        if '3' in str(mm):
            count += 60
            continue
        for ss in range(60):
            if '3' in str(ss):
                count += 1

print(count)  # 결과 출력

''' 입력 예시 1
5
'''
''' 출력 예시 1
11475
'''