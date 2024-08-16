from collections import deque

q = deque()
for i in range(1000000):
    q.append(i)
for _ in range(1000000):
    q.popleft()
print('end')

# list_q = []
# for i in range(1000000):
#     list_q.append(i)
# for _ in range(1000000):
#     list_q.pop(0)
# print('end')