# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]  # 초기 풍선
            for k in range(4):
                for num in range(1, arr[i][j] + 1):
                    ni = i + di[k] * num
                    nj = j + dj[k] * num
                    if 0 <= ni < N and 0 <= nj < M:
                        cnt += arr[ni][nj]
            if result < cnt:
                result = cnt

    print(f'#{tc}', result)