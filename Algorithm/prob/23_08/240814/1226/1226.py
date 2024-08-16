import sys

sys.stdin = open('input.txt')

from collections import deque

def bfs(i, j, N):
    # 준비
    visited = [[0]*N for _ in range(N)]   # visited 생성
    q = deque()         # 큐 생성
    q.append([i, j])    # 큐 인큐
    visited[i][j] = 1   # 시작점 visited 표시

    # 탐색
    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            wi, wj = ti+di, tj+dj
            if 0<=wi<N and 0<=wj<N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                visited[wi][wj] = visited[i][j] + 1
                q.append([wi, wj])
    return 0

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

# Testcase 만큼 반복
for _ in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    ti, tj = find_start(16)

    print(f'#{tc}', bfs(ti, tj, 16))