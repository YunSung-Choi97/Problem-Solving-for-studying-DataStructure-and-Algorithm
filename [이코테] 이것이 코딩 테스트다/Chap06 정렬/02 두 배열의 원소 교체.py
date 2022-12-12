n, k = map(int, input().split())  # 배열의 크기, 바꿔치기 연산 횟수

arrayA = list(map(int, input().split()))  # A 배열
arrayB = list(map(int, input().split()))  # B 배열

arrayA.sort()  # 오름차순 정렬
arrayB.sort(reverse=True)  # 내림차순 정렬

# 바꿔치기 연산
for i in range(k):
    if arrayA[i] < arrayB[i]:
        arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
    else:
        break

print(sum(arrayA))  # 결과 출력

''' 입력 예시 1
5 3
1 2 5 4 3
5 5 6 6 5
'''
''' 출력 예시 1
26
'''