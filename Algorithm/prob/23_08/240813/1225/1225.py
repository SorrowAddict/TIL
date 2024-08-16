import sys
from collections import deque

sys.stdin = open('input.txt')

def create_pwd(lst):
    minus_value = 1     # 뺴줄 값을 초기 지정
    while 1:            # 반복문을 통해 반복 (재귀함수 구조 사용 실패 ㅠ)
        # popleft()에서 minus_value를 빼서 저장
        temp = lst.popleft() - minus_value
        minus_value += 1        # 시행 후엔 minus_value를 1 증가
        if temp <= 0:           # temp 값이 0보다 작거나 같으면
            temp = 0            # 0으로 고정 후 append(), 종료함
            lst.append(temp)
            break
        # minus 값이 5를 초과하면 1로 재지정 해주는 부분
        if minus_value > 5:
            minus_value = 1
        lst.append(temp)        # temp가 0보다 크면 정상적으로 append()
    return lst

# Testcase 만큼 반복
for _ in range(10):
    tc = int(input())
    arr = deque(list(map(int, input().split())))

    print(f'#{tc}', *create_pwd(arr))