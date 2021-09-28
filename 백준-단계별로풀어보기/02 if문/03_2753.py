year = int(input())  # year : 연도를 입력받음

# 문제의 조건에 맞게 조건식을 세워 윤년과 윤년이 아닌 해를 구분
if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
    print(1)
else:
    print(0)