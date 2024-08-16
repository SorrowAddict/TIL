# 4615. 재미있는 오셀로 게임

def f(i, j, color, N):
    board[i][j] = color
    for di, dj in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]:
        ni, nj = i+di, j+dj
        temp = []       # 뒤집을 돌의 인덱스를 저장
        while 0<=ni<N and 0<=nj<N and board[ni][nj]==op[color]:
            temp.append((ni, nj))   # 뒤집을 돌을 저장
            ni, nj = ni+di, nj+dj   # 현재 방향으로 계속 이동
        if 0<=ni<N and 0<=nj<N and board[ni][nj] == color:
            for p, q in temp:
                board[p][q] = color

# 1이면 흑돌, 2이면 백돌
B, W = 1, 2
op = [0, 2, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 배열의 크기 N, 돌을 놓는 횟수 M
    play = [list(map(int, input().split())) for _ in range(M)]

    board = [[0]*N for _ in range(N)]   # NxN board 준비, 0 -> N-1 인덱스 사용
    # 중심부 돌을 배치
    # WB
    # BW
    board[N//2-1][N//2-1] = W
    board[N//2][N//2-1] = B
    board[N//2][N//2] = W
    board[N//2-1][N//2] = B

    # 돌 놓기
    for col, row, color in play:
        f(row-1, col-1, color, N)

    bcnt = wcnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                bcnt += 1
            elif board[i][j] == W:
                wcnt += 1

    print(f'#{tc}', bcnt, wcnt)