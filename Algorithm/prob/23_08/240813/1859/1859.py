import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0

    # 리스트를 거꾸로 순회
    for i in range(N-1, 0, -1):
        if arr[i] > arr[i-1]:           # 이전값이 작을때만
            result += arr[i]-arr[i-1]   # 값의 차이를 결과값에 추가
            arr[i-1] = arr[i]           # 이전값을 비교값으로 바꾸기 (큰 값으로)

    print(f'#{tc}', result)