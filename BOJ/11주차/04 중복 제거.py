import sys

# data = sys.stdin.readline().split()
# count = dict()

# for num in data:
#     try:
#         count[num] += True
#     except:
#         count[num] = True
#         print(num, end=' ')

# data = list(map(int, input().split()))
# exist = [False] * pow(2, 25)
# for num in data:
#     if exist[num]:
#         continue
#     else:
#         print(num, end=' ')
#         exist[num] = True

a = '0' * 21
c = [a, False]
print(sys.getsizeof(a))
print(sys.getsizeof(c))