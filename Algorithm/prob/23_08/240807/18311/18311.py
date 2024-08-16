import sys

sys.stdin = open('input.txt')

def DFS(s, V):      # 시작점 ~ 점개수
    visited = [0] * (V+1)
    stack = []
    print(s, end='')
    visited[s] = 1
    v = s
    while 1:
        for w in adjL[v]:
            if visited[w] == 0:
                stack.append(v) # 왔던 길 스택에 추가
                v = w
                print(f'-{v}', end='')
                visited[w] = 1  # 지나간 길 체크
                break
        else:
            if stack:       # 되돌아갈 길이 남아있으면 되돌아가기
                v = stack.pop()
            else:           # 되돌아갈 길이 없으면 전체 반복 종료
                break

V, E = map(int, input().split())
adjL = [[] for _ in range(V+1)]
arr = list(map(int, input().split()))
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adjL[v1].append(v2)
    adjL[v2].append(v1)

print('#1', end=' ')
DFS(1, V)