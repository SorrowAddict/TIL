'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, V):      # 시작점s, 마지막 정점V    
    # 준비
    visited = [0]*(V+1)     # visited 생성
    q = []          # 큐 생성
    q.append(s)     # 시작점 인큐
    visited[s] =1   # 시작점 방문 표시

    # 탐색
    while q:        # 탐색할 정점이 남아있으면
        t = q.pop(0)    # t <- 디큐
        print(t, end= ' ')        # 처리
        for w in adj_l[t]: # t에 인접이고, 인큐된적이 없으면
            if not visited[w]:
                q.append(w) # 인큐하고 인큐됨 표시
                visited[w] = visited[t] + 1
    # 최단거리를 체크할 수도 있음
    # print(visited)
    

V, E = map(int, input().split())    # V 정점의 개수, E 인접 노드의 개수
arr = list(map(int, input().split()))

adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)        # 방향이 없으면 양방향

print('#1', end=' ')
bfs(1, V)   # 출발점, 정점수