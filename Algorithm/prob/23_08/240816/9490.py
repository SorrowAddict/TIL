# 9490. 풍선팡

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            temp = arr[i][j]
            for di, dj in [[0 ,1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i, j
                for k in range(arr[i][j]):
                    ni += di
                    nj += dj
                    if 0<=ni<N and 0<=nj<M:
                        temp += arr[ni][nj]
            result = max(result, temp)
    print(f'#{tc} {result}')