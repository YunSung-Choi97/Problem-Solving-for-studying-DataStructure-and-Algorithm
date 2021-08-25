# 이것이 "취업을 위한" 코딩테스트다 (with 파이썬)

나동빈 저자의 교재 "이것이 취업을 위한 코딩테스트다"에 대한 학습 내용을 작성한 repository이다.<br>
내용은 교재 내용, 강의 내용(나동빈 유투브), 스스로 풀어본 소스 코드, 주어진 솔루션을 기반으로 제작되었다.<br>

<br>

## 코딩 테스트 준비

### 다양한 온라인 저지 사이트

1. 해외 사이트
 - 코드포스 : http://www.codeforces.com
 - 탑코더 : https://www.topcoder.com
 - 릿코드 : https://www.leetcode.com
 - 코드셰프 : https://www.codechef.com

2. 국내 사이트
 - 백준 : https://www.acmicpc.net
 - 코드업 : https://codeup.kr
 - 프로그래머스 : https://programmers.co.kr
 - SW Expert Academy : https://swexpertacademy.com

### 파이썬 시간 초과 예상 및 설계

1. Python 사용시 1초에 약 50,000,000번의 연산이라고 예상(채점용 서버에서는 1초에 약 20,000,000번이라고 예상)하고 문제에 접근
 - 이는 환경에 따라 차이가 존재

2. 시간제한이 1초인 경우
 - N의 범위가 500 : O(N^3) 이내로 설계
 - N의 범위가 2,000 : O(N^2) 이내로 설계
 - N의 범위가 100,000 : O(NlonN) 이내로 설계
 - N의 범위가 10,000,000 : O(N) 이내로 설계

3. 수행 시간 측정
```python
import time

start_time = time.time()
# 프로그램 소스코드
end_time = time.time()

print("time : ", end_time - start_time)
```