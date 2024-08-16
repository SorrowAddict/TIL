'''
5
45 15 10 56 23
96 98 99 48 69
96 84 49 46 34
16 64 81 4 11
10 66 85 55 14
'''

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    total = 0
    for i in range(N):
        for j in range(N):  # NxN 배열의 모든 원소에 대해
            s = 0           # 문제에서 원소와 주변 인접 원소의 차의 ...
            # i, j 원소의 4방향 원소에 대해
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    s += abs(arr[i][j] - arr[ni][nj])
            total += s
    print(f'#{tc} {total}')