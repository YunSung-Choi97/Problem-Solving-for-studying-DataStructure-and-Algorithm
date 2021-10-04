'''미리 생각하기
1. 입력받기
 1-1. t : test case 수
 1-2. Sm, Sc, Si : 메모리(배열) 크기, 프로그램 코드의 크기, 입력의 크기
 1-3. code : 프로그램 코드
 1-4. input_val : 프로그램 입력 문자열
2. 동작 구현
3. 반복문 진입 상태 저장 후 재진입할 때와 비교
'''

import sys
from collections import deque

# 주어진 프로그램에 맞게 실행하도록 설계
def Brainf_k():
    global loc, p, Sc
    if code[loc] == '-':
        array[p] = (array[p] - 1) % 256  # unsigned 8-bit이기 때문에 값은 0 ~ 255
    elif code[loc] == '+':
        array[p] = (array[p] + 1) % 256  # unsigned 8-bit이기 때문에 값은 0 ~ 255
    elif code[loc] == '<':
        p = (p - 1) % Sm
    elif code[loc] == '>':
        p = (p + 1) % Sm
    elif code[loc] == '[':
        # ']' 인덱스로 이동
        if array[p] == 0:
            for i in range(len(loop)):
                if loop[i][0] == loc:
                    loc = loop[i][1]
                    break
    elif code[loc] == ']':
        # '[' 인덱스로 이동
        if array[p] != 0:
            for i in range(len(loop)):
                if loop[i][1] == loc:
                    loc = loop[i][0]
                    break
    elif code[loc] == '.':
        pass  # 출력은 무한루프 판정과 관련이 없으므로 무시 가능
    elif code[loc] == ',':
        global idx
        if idx < Si:
            data = ord(input_val[idx])
            idx += 1
        else:
            data = 255
        array[p] = data

t = int(input())
for _ in range(t):
    # 입력받기
    Sm, Sc, Si = map(int, sys.stdin.readline().split())
    code = list(sys.stdin.readline().rstrip())
    input_val = list(sys.stdin.readline().rstrip())
    
    # 초기화
    loc = 0  # 프로그램에서 현재 실행 중인 코드의 위치
    array = [0] * Sm  # 배열
    p = 0  # 배열 포인터
    idx = 0
    loop = []  # loop [ ]의 (시작, 끝) 인덱스
    temp = []  # stack
    for i in range(Sc):  # 스택 형태를 이용해 '['와 ']' 쌍의 위치 찾기
        if code[i] == '[':
            temp.append(i)
        elif code[i] == ']':
            loop.append((temp.pop(), i))
    
    flag = True  # 무한 루프 판정
    if not loop:  # '[', ']'가 없는 경우
        flag = False
    loop_start = Sc  # 무한 루프일 경우 무한 루프 시작인덱스를 저장
    count = 0  # 명령어 수행 횟수
    while flag:
        Brainf_k()
        loc += 1
        if loc == Sc:  # 모든 코드 실행
            flag = False
            break
        
        count += 1
        if count > 100000000:  # 최대 명령어 초과
            break
        elif count > 50000000:  # 무한 루프인 경우의 최소 인덱스
            loop_start = min(loop_start, loc-1)
    
    if flag:
        for i in range(len(loop)):
            if loop[i][0] == loop_start:
                loop_end = loop[i][1]
                break
        print('Loops {} {}'.format(loop_start, loop_end))
    else:
        print('Terminates')