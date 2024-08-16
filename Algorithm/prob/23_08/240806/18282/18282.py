import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = input().rstrip()
    result = 1      # 결과 초기값 1

    # stack 검증을 위한 리스트 생성
    check_list = []
    for x in N:
        if x == '(':    # ( 이면 stack에 push
            check_list.append(x)
        elif x == ')':  # ) 이면
            if len(check_list) == 0:    # stack이 비어있으면 -1을 반환하고 break
                result = -1
                break
            elif check_list.pop() != '(':   # stack에서 pop한 결과가 (가 아니면 -1, break
                result = -1
                break
    # for문으로 전체순회가 다 돌아가고 stack에 남아있는 게 있으면 -1
    if len(check_list) > 0:
        result = -1

    print(f'#{tc}', result)