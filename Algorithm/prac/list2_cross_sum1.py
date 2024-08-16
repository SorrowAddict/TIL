# import sys
#
# sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    # 5x5 2차원 배열에 입력값 저장
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 대각선 원소의 합 초기값 설정
    cross_sum = 0

    # 2차원 배열 전체 순회
    for i in range(5):
        for j in range(5):
            # i==j인 대각선이거나 4-i==j 인 대각선의 값을 cross_sum에 += 연산
            if (i == j) or (4-i == j):
                cross_sum += arr[i][j]

    print(f'#{tc} {cross_sum}')