import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = []

    # 입력받은 배열 탐색
    for i in arr:
        for j in range(N-M+1):              # N-M 만큼 예) 15 10 이면 10칸씩 5만큼
            test = i[j:j + M]
            if test[:] == test[::-1]:       # 뒤집어서 같으면
                result.append(i[j:j+M])     # 결과에 추가

    # 열 검색을 위한 배열 생성
    new_arr = [[0]*N for _ in range(N)]
    # 대칭 행렬 생성
    for i in range(N):
        for j in range(N):
            new_arr[j][i] = arr[i][j]

    # 생성된 대칭 행렬 탐색
    for i in new_arr:
        for j in range(N-M+1):              # N-M 만큼 예) 15 10 이면 10칸씩 5만큼
            test = i[j:j + M]
            if test[:] == test[::-1]:       # 뒤집어서 같으면
                result.append(i[j:j+M])     # 결과에 추가

    print(f'#{tc}', ''.join(result[0]))