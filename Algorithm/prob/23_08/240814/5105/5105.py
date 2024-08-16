#5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

import sys

sys.stdin = open('input.txt')

from collections import deque

# Testcase 수
T = int(input())

def bfs(i, j, N):
    # 탐색
    visited = [[0]*(N) for _ in range(N)]      # visited 생성
    q = deque()             # 큐 생성
    q.append([i, j])        # 시작점 인큐
    visited[i][j] = 1       # 시작점 방문 표시

    # 탐색
    while q:
        ti, tj = q.popleft()    # 방문점 디큐
        if maze[ti][tj] == 3:
            return visited[ti][tj] - visited[i][j] -1
        # 미로범위내, 방문X, 벽이 아니면
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            wi, wj = ti+di, tj+dj
            if 0<=wi<N and 0<=wj<N and visited[wi][wj] == 0 and maze[wi][wj] != 1:
                q.append([wi, wj])  # 방문가능점 인큐
                visited[wi][wj] = visited[ti][tj] + 1   # 인큐 표시
    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    si, sj = find_start(N)

    print(f'#{tc}', bfs(si, sj, N))