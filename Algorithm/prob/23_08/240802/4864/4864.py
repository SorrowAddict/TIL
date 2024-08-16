import sys

sys.stdin = open('input.txt')

def my_len(lst):
    cnt = 0
    for _ in lst:
        cnt += 1
    return cnt

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    # str 입력을 list로 변환
    key = list(input())
    arr = list(input())

    # 전체 arr 리스트 길이에서 체크할 key 리스트 길이를 뺀 만큼 순회하면서
    # i ~ i+ (key리스트 길이값) 이 key와 일치하는 지 체크
    result = 0
    for i in range(my_len(arr)-my_len(key)):
        if arr[i:i+my_len(key)] == key:
            result = 1

    print(f'#{tc}', result)