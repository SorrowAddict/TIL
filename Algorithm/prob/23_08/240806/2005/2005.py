import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    # #{tc} 먼저 출력
    print(f'#{tc}')

    N = int(input())
    # 행 별로 파스칼의 삼각형을 저장하기 위한 2차원 배열 생성
    arr = [[] for _ in range(11)]

    for i in range(1, N+1):
        # 1, 2일 때의 예외 처리
        if i == 1 or i == 2:
            arr[i] = [1] * i

        # 1, 2가 아닐 때의 파스칼의 삼각형 2차원 배열에 저장
        else:
            value = []      # 최외각의 1을 제외한 중간 값을 저장
            # 윗행을 순회
            for idx, v in enumerate(arr[i-1]):
                if 0 <= idx < len(arr[i-1])-1:  # 탐색 범위 0 ~ -2 까지
                    # 초기값부터 그 다음값을 더한 값을 value에 추가
                    value.append(arr[i-1][idx]+arr[i-1][idx+1])
            arr[i] = [1, *value, 1]     # 해당 행을 최외각 1값과 함께 저장
        print(*arr[i])      # 리스트로 저장하였기에 저장한 현재행을 언패킹으로 출력