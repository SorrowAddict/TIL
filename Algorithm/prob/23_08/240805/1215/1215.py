import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10

# Testcase 만큼 반복
for tc in range(1, T+1):
    length = int(input())
    arr = [list(input()) for _ in range(8)]
    result = 0

    # 가로 탐색
    for i in range(8):
        for j in range(8-length+1):     # 가로 인덱스가 안넘어가는 조건
            # 리스트의 인덱싱과 list(reversed()) 함수 사용해서 회문 비교
            if arr[i][j:j+length] == list(reversed(arr[i][j:j+length])):
                result += 1

    # 세로 탐색
    for j in range(8):
        for i in range(8-length+1):
            # 세로의 경우 인덱싱이 안되기 때문에 "".join을 for문을 통해 str로 추출
            check = "".join([arr[i + k][j] for k in range(length)])
            # 회문인지 체크
            if check == check[::-1]:
                result += 1

    print(f'#{tc}', result)