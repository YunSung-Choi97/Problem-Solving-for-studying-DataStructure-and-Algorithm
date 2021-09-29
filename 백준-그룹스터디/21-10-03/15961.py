'''미리 생각하기
1. 입력받기
 1-1. N, d, k, c 
 1-2. 벨트 위 초밥 종류 저장 >> 크기가 N인 리스트 >> 앞쪽 k개를 뒤에 연결해 연결된 벨트처럼 구현
2. 투 포인터(left, right) 사이의 초밥 가짓수를 알아낸 후 한칸씩 이동
3. 포인터 사이에 쿠폰 번호 메뉴가 있는지 확인
'''

import sys

# 입력받기
belt_size, menu_size, eat_size, coupon = map(int, input().split())
belt = [int(sys.stdin.readline()) for _ in range(belt_size)]
belt += belt[:eat_size-1]

# left와 right 사이의 먹은 초밥 데이터와 가짓수 저장
left, right = 0, eat_size-1
eat = [0 for _ in range(menu_size+1)]
menu_count = 0
for i in range(left, right+1):
    # 새로운 종류의 초밥을 먹는 경우
    if eat[belt[i]] == 0:
        menu_count += 1
    # 먹은 초밥 데이터 저장
    eat[belt[i]] += 1

answer = 0
# 한칸씩 이동
while right + 1 <= belt_size + eat_size - 2:  # 이동할 오른쪽 인덱스 <= 벨트의 마지막 인덱스
    # 먹을 범위 한칸씩 이동
    delete = belt[left]  # 범위에서 빠지는 초밥
    left += 1
    right += 1
    update = belt[right]  # 범위로 들어오는 초밥

    # 먹은 초밥 데이터, 가짓수 업데이트
    if eat[delete] == 1:
        menu_count -= 1
    eat[delete] -= 1
    if eat[update] == 0:
        menu_count += 1
    eat[update] += 1

    # 쿠폰 메뉴 확인
    if eat[coupon] == 0:
        # answer = max(answer, menu_count + 1)  # 변경 전 코드
        if answer < menu_count + 1:
            answer = menu_count + 1
        if answer == eat_size + 1:  # eat_size + 쿠폰 하나 보다 큰 값은 나올 수 없기 때문에
            break
    else:
        # answer = max(answer, menu_count)  # 변경 전 코드
        if answer < menu_count:
            answer = menu_count

# 정답 출력
print(answer)