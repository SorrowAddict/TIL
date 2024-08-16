# 1. 끝(시작지점)인 2값을 찾기
# 2. 역으로 올라가면서 (99번째 행부터 0번째 행까지)
# 3. 좌우열에 1이 존재하면 0이 나오기 전까지 이동
# 4. 다시 위로 올라가면서 2~3을 반복
# 5. 0번째 행의 값을 출력

import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10
# Testcase 만큼 반복
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 좌우열 이동 변동값
    dj = [1, -1]

    # 시작지점 찾기
    idx = 0
    for i in arr[99]:
        if i == 2:
            col = idx
        idx += 1

    # 98번째 행부터 0번째 행까지
    row = 99
    while row > 0:
        row -= 1

        # 좌우열에 1이 존재하는지 체크하고 존재한다면 0이 나오기 전까지 이동
        # 우측
        if (0 <= col + dj[0] < 100) and (arr[row][col + dj[0]] == 1):
            nj = col + dj[0]
            while (0 <= nj < 100) and (arr[row][nj] == 1):
                nj += dj[0]
                if 0 > nj or nj >= 100:
                    nj -= dj[0]
                    col = nj
                    break
                elif arr[row][nj] == 0:
                    col = nj - dj[0]

        # 좌측
        elif (0 <= col + dj[1] < 100) and (arr[row][col + dj[1]] == 1):
            nj2 = col + dj[1]
            while (0 <= nj2 < 100) and (arr[row][nj2] == 1):
                nj2 += dj[1]
                if 0 > nj2 or nj2 >= 100:
                    nj2 -= dj[1]
                    col = nj2
                    break
                elif arr[row][nj2] == 0:
                    col = nj2 - dj[1]

    print(f'#{tc} {col}')