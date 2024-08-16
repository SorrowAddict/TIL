# 1. 전체 리스트를 순회하면서 동일한 기호가 2번 이상 나올 때마다 카운트 추가
#    다른 기호가 나올때까지 누적합, 다른 기호가 나오면 result에 추가 후 초기화
# 2. 2번 같은 기호가 나오면 기호 간의 합이 같아질 때까지 리스트를 저장하면서
#    리스트 속의 ()의 개수를 체크하고 그 개수의 -1 만큼 result에 추가한다.

import sys

sys.stdin = open('input.txt')

def my_len(lst):
    cnt_lst = 0
    for _ in lst:
        cnt_lst += 1
    return cnt_lst

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    arr = input()
    result = 0
    cnt = 0

    for i in range(my_len(arr)):
        if i > 0:
            if arr[i] == '(':
                cnt += 1
            elif arr[i] == ')':
                cnt -= 1
            if arr[i] == ')' and arr[i-1] == '(':
                result += cnt
            elif arr[i] == ')' and arr[i-1] == ')':
                result += 1
        else:
            if arr[i] == '(':
                cnt += 1

    print(f'#{tc}', result)