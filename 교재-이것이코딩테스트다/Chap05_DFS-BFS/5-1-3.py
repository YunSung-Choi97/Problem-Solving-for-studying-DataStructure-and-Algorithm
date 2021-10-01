# 종료 조건이 없는 재귀함수가 호출되어 무한히 출력이 이루어진다.
# 어느 정도 출력하다가 재귀의 최대 깊이를 초과하여 에러가 발생한다.

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()