# 해결 X

# N, M = map(int, input().split())
# Hn = list(map(int, input().split()))
# Hn.sort()
# result = dict()

# def bi_search(start, end):
#     mid = (start + end) // 2

#     value = 0
#     for i in range(mid, end):
#         if result.get(i) == None:
#             value += Hn[i]
#         else:
#             value += result.get(i)
#             break
#     if value >= M:
#         bi_search(mid, end)
#     else:
#         result[mid] = value
#         bi_search((start + mid) // 2, end)