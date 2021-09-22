import sys
input = sys.stdin.readline

N = int(input())
X_data = list(map(int, input().split()))  # 입력받은 X 정보. (X1, X2, ..., Xn)
sorted_X_data = sorted(set(X_data))  # X 정보를 중복제거한 뒤 오름차순 정렬
X_Xc = {sorted_X_data[i] : i for i in range(len(sorted_X_data))}  # 값과 압축결과를 연결

# 압축결과를 하나씩 출력.  (2가지 방법)
# for i in X_data:
#     print(X_Xc[i], end=' ')
print(*[X_Xc[i] for i in X_data])