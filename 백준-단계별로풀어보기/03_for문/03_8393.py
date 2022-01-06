n = int(input())  # n : 합할 수의 마지막 값을 입력받음
result = 0  # result : 합한 최종 결과

for i in range(1, n+1):  # 1부터 n까지.
    result += i  # result = result + i
    
print(result)