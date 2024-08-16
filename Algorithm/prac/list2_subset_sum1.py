# sum() 함수 생성
def my_sum(lst):
    sum_v = 0
    for x in lst:
        sum_v += x
    return sum_v

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    n = len(arr)
    # 부분 집합을 저장할 변수 리스트 생성
    sub_set = []
    # n개의 모든 부분 집합의 개수만큼 순회
    for i in range(1<<n):
        s = []      # 부분 집합 내부 리스트 생성
        for j in range(n):
            if i & (1<<j):
                s.append(arr[j])    # 각 부분 집합 내부 리스트 생성
        # 생성된 부분 집합 내부 리스트의 합이 0일 때 저장
        if my_sum(s) == 0:
            sub_set.append(s)

    # 합이 0인 부분 집합 이 존재하는 지 체크
    if len(sub_set) >= 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')