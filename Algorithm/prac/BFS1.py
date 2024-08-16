# 중복 노드에 대한 중복 정점 enQ를 맨 아래 2줄에서 중복 체크
# enQ 기준 : 처리 완료를 기준으로

def BFS(G, v):      # 그래프 G, 탐색 시작점 v
	visited = [0] * (n+1)   # n : 정점의 개수
    queue = []              # 큐 생성
    queue.append(v)         # 시작점 v를 큐에 삽입
    while queue:                # 큐가 비어있지 않은 경우
        t = queue.pop(0)        # 큐의 첫 번째 원소 반환
        if not visited[t]:  # 방문되지 않은 곳이라면
            visited[t] = True   # 방문한 것으로 표시
            visit(t)        # 정점 t에서 할 일
            for i in G[t]:      #t와 연결된 모든 정점에 대해
                if not visited[i]:  # 방문되지 않은 곳이라면
                    queue.append(i)     # 큐에 넣기