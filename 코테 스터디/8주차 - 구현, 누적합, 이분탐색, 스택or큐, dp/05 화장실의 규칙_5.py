# import sys
# input = sys.stdin.readline

# def priority(array):
#     heap = []
#     heap.append(array[0])
#     for i in range(1, len(array)):
#         item = array[i]
#         idx = i
#         heap.append(item)
#         while True:
#             if idx == 0:
#                 heap[0] = item
#                 break
#             elif idx % 2 == 0:
#                 if item > heap[idx//2-1]:
#                     heap[idx] = heap[idx//2-1]
#                     idx = idx//2-1
#                 else:
#                     heap[idx] = item
#                     break
#             else:
#                 if item > heap[idx//2]:
#                     heap[idx] = heap[idx//2]
#                     idx = idx//2
#                 else:
#                     heap[idx] = item
#                     break
#     result = []
#     for i in range(len(heap)-1):
#         result.append(heap[0])
#         item = heap[-1]
#         heap[0] = item
#         del heap[-1]
#         idx = 0
#         last = len(heap)-1
#         while True:
#             if idx*2+1 > last:  # 자식노드 없는 경우
#                 heap[idx] = item
#                 break
#             elif (idx+1)*2 > last:  # 자식노드가 left만 존재
#                 if item < heap[idx*2+1]:
#                     heap[idx] = heap[idx*2+1]
#                     idx = idx*2+1
#                 else:
#                     heap[idx] = item
#                     break
#             elif heap[idx*2+1] > heap[(idx+1)*2]:
#                 if item < heap[idx*2+1]:
#                     heap[idx] = heap[idx*2+1]
#                     idx = idx*2+1
#                 else:
#                     heap[idx] = item
#                     break
#             elif heap[idx*2+1] < heap[(idx+1)*2]:
#                 if item < heap[(idx+1)*2]:
#                     heap[idx] = heap[(idx+1)*2]
#                     idx = (idx+1)*2
#                 else:
#                     heap[idx] = item
#                     break
#     result.append(heap[0])
#     return result

# a = [1, 2, 3, 4, 6, 8, 5]

# print(priority(a))

from queue import PriorityQueue

que = PriorityQueue()

a = (0, (0, 0))
b = (2, (0, 1))
c = (1, (1, 0))
d = (2, (1, 1))
e = (3, (2, 0))
f = (2, (2, 1))

que.put(a)
que.put(b)
que.put(c)
que.put(d)
que.put(e)
que.put(f)

print(que.get())
print(que.get())
print(que.get())
print(que.get())
print(que.get())