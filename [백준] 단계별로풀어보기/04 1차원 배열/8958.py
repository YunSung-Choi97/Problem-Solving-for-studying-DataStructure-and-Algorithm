T = int(input())  # 테스트 케이스의 개수

for _ in range(T):
    result = input()    # 퀴즈의 결과
    count = 0           # 현재 문제의 점수
    score = 0           # 퀴즈 전체의 점수

    # 문자열을 한 글자씩 읽어와 맞춘 경우 현재문제 점수를 1점 더한 후, 현재 점수를 전체 점수에 더하는 방식
    for j in range(len(result)):
        if result[j] == "O":
            count += 1
        else:
            count = 0
        score += count
    
    print(score)