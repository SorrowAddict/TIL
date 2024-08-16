#5102. [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리

import sys

sys.stdin = open('input.txt')

from collections import deque

def bfs(s, G, V):
    # 준비
    visited = [0]*(V+1)     # visited 생성
    q = deque()             # 큐 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 지나간 곳 표시

    # 탐색
    while q:
        t = q.popleft()         # 탐색점 디큐 저장
        if t == G:
            return visited[t] - visited[s]
        for i in adj_l[t]:    # 인접한 정점 중
            if not visited[i]:  # 방문하지 않은 곳이면
                q.append(i)     # 인큐
                visited[i] = visited[t] + 1 # 지나간 곳 표시
    return 0

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    adj_l = [[] for _ in range(V+1)]
    for v1, v2 in arr:
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)
    S, G = map(int, input().split())

    print(f'#{tc}', bfs(S, G, V))