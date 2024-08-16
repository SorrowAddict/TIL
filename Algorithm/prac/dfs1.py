'''
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''
def DFS(s, V):              # s시작정점, v 정점개수(1번부터인 정점의 마지막정점)
    visited = [0] * (V+1)   # 방문한 정점을 표시
    stack = []              # 스택생성
    print(s)
    visited[s] = 1          # 시작 정점 방문 표시
    v = s
    while 1:
        for w in adjL[v]:       # v에 인접하고, 방문안한 w가 있으면
            if not visited[w]:
                visited[w] = 1  # w에 방문 표시
                stack.append(v) # push(v) 현재 정점을 push하고
                v = w           # w에 방문
                print(v)
                break           # for w: break / v부터 다시 탐색
        else:                   # 남은 인접 정점이 없어서 break가 걸리지 않은 경우
            if stack:       # 이전 갈림길을 스택에서 꺼내서... if TOP > -1
                v = stack.pop()
            else:           # 되돌아갈 곳이 없으면 남은 갈림길이 없으면 탐색 종료
                break       # while 1: break

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    for i in range(E):
        v1, v2 = arr[i*2], arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    print(adjL)

    DFS(1, V)