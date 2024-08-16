import sys
input = sys.stdin.readline

N = int(input())
L = []
for _ in range(N):
    start, end = map(int, input().split())
    L.append([start, end])
L.sort(key= lambda x: ((x[0], x[1]), L))

print(L)

for s, e in L:
    print(s, e)