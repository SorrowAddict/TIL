# 1. 받은 N값으로 1~N^2 만큼 리스트를 만듬
# 2. 오른쪽 방향부터 시계방향으로 가되, 다음의 규칙으로 델타 뱡향을 바꾼다.
#   2-1. 범위를 벗어날 때
#   2-2. 이미 값이 존재할 때
# 3. 이동하는 while 반복문이 끝나면 배열을 출력한다.

import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    num_list = [i for i in range(N * N, 0, -1)]

    i = j = 0
    k = 0  # 방향 인덱스

    while num_list:
        arr[i][j] = num_list.pop()
        ni = i + di[k % 4]
        nj = j + dj[k % 4]

        # 다음 위치가 유효한지 확인
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            # 방향 전환
            k += 1
            i += di[k % 4]
            j += dj[k % 4]

    # 배열 출력
    print(f'#{tc}')
    for row in arr:
        print(' '.join(map(str, row)))