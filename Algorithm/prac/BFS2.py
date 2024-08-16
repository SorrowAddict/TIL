# enQ 단계에서 중복을 방지
# enQ 기준 : 인접 기준으로

def BFS(G, v, n):      # 그래프 G, 탐색 시작점 v
	visited = [0] * (n+1)   # n : 정점의 개수
    queue = []              # 큐 생성
    queue.append(v)         # 시작점 v를 큐에 삽입
    visited[v] = 1          # enQ 표시함 ### 이 부분 중요 ###
    while queue:                # 큐가 비어있지 않은 경우
        t = queue.pop(0)        # 큐의 첫 번째 원소 반환
        print(t)
        for i in G[t]:      #t와 연결된 모든 정점에 대해
            if not visited[i]:  # 방문되지 않은 곳이라면
                queue.append(i)     # 큐에 넣기
                visited[i] += 1     # n으로 부터 1만큼 이동