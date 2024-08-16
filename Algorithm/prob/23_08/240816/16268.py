#16268. 풍선팡 2

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            temp = arr[i][j]
            for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:
                for k in range(1, 2):
                    ni, nj = i + di*k, j + dj*k
                    if 0<=ni<N and 0<=nj<M:
                        temp+=arr[ni][nj]
            else:
                max_v = max(max_v, temp)
    print(f'#{tc} {max_v}')