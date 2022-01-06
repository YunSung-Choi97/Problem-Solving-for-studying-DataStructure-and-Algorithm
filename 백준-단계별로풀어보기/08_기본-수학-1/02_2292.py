N = int(input())

# 벌집은 칸마다 최대 1, 7, 19, 37, 61, ... 번 방까지 찾아갈 수 있다.
# 이는 1부터 6, 12, 18, 24, ... 즉 칸마다 6의 배수씩 방의 개수가 늘어난다.

result = 0  # 결과 (지나는 방의 수)
layer = 1   # result에 따라 총 몇 번째 방까지 포함되는지 확인
while True:
    layer += 6 * result
    if N <= layer:
        print(result+1)
        break
    else:
        result += 1

