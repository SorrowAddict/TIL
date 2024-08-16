import sys

sys.stdin = open('input.txt')

from collections import deque

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())

    L = deque(list(map(int, input().split())))
    arr = deque()

    # 몇 번째 피자인지 인덱스 표시
    for i in range(1, N+1):
        arr.append([L.popleft(), i])

    while len(arr) > 1:
        # 1번을 꺼내고 치즈가 녹음
        temp = arr.popleft()
        temp[0] //= 2
        # 치즈가 다 녹았다면 화덕에서 꺼내고 그 자리에 남은 피자를 넣기
        if temp[0] == 0:
            if len(L) > 0:
                # 리스트 속에 인덱스 번호를 추가하여 그 자리에 피자 넣기
                N += 1      # N의 초기값만큼은 위 for문에서 다 돌아갔기 때문에 +1
                arr.appendleft([L.popleft(), N])
        else:
            arr.append(temp)

    print(f'#{tc}', arr[0][1])

#1 deque([[1, 4]])
#2 deque([[1, 8]])
#3 deque([[1, 6]])