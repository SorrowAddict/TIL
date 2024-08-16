import sys
input = sys.stdin.readline

N = int(input())
lst = [0] * 10000
for _ in range(N):
    lst[int(input())-1] += 1
for i in range(1, len(lst)+1):
    for _ in range(lst[i-1]):
        print(i)
# for i, v in enumerate(lst):
#     for _ in range(v):
#         print(i+1)