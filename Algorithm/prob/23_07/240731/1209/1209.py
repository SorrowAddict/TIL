import sys

sys.stdin = open('input.txt')

def my_max(lst):
    max_v = lst[0]
    for x in lst:
        if max_v <= x:
            max_v = x
    return max_v

# Testcase 만큼 반복
for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 초기 최댓값 설정
    max_num = 0
    cross_sum = 0
    # 행, 열, 대각선 합 순회
    for i in range(100):
        row_sum = 0
        col_sum = 0
        cross_sum += arr[i][i]      # 대각선 합
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]
        max_check = my_max([row_sum, col_sum])  # 행, 열 합의 최댓값 계산
        if max_num <= max_check:
            max_num = max_check                 # 최댓값 업데이트
    max_check2 = my_max([max_num, cross_sum])   # 행, 열 합의 최댓값과 대각선합 최댓값 체크
    if max_num <= max_check2:
        max_num = max_check2                    # 최종 최댓값 업데이트

    print(f'#{tc} {max_num}')