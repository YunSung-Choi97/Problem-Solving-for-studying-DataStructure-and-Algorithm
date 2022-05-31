a, b, c = map(int, input().split())  # 주사위 눈 3개 입력받기

if a == b and b == c:  # 모두 같은 경우
  ans = 10000 + a * 1000
elif a == b or a == c:  # 두개만 같은 경우
  ans = 1000 + a * 100
elif b == c:  # 두개만 같은 경우
  ans = 1000 + b * 100
else:  # 모두 다른 경우
  ans = max(a, b, c) * 100

print(ans)  # 상금 출력