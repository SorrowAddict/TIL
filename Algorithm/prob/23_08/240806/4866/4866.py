import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = input()
    preprocessed_texts = []
    key_list = ['(', ')', '{', '}']
    for x in N:
        if x in key_list:
            preprocessed_texts.append(x)

    check_list = []
    result = 1
    for x in preprocessed_texts:
        if x == '(':    # ( 이면 stack에 push
            check_list.append(x)
        elif x == ')':  # ) 이면
            if len(check_list) == 0:    # stack이 비어있으면 -1을 반환하고 break
                result = 0
                break
            elif check_list.pop() != '(':   # stack에서 pop한 결과가 (가 아니면 0, break
                result = 0
                break
        if x == '{':    # { 이면 stack에 push
            check_list.append(x)
        elif x == '}':  # } 이면
            if len(check_list) == 0:    # stack이 비어있으면 0을 반환하고 break
                result = 0
                break
            elif check_list.pop() != '{':   # stack에서 pop한 결과가 {가 아니면 0, break
                result = 0
                break
    # for문으로 전체순회가 다 돌아가고 stack에 남아있는 게 있으면 -1
    if len(check_list) > 0:
        result = 0

    print(f'#{tc}', result)