import sys

sys.stdin = open('input.txt')

# Testcase 만큼 반복
for tc in range(1, 11):
    l = int(input())
    N = input()

    # ------ 후위표기법 전환 ------ #
    # 후위표기법, 스택을 저장할 리스트 생성
    postfix, stack = [], []

    for x in N:
        if x.isnumeric():   # 숫자를 만나면 push
            postfix.append(x)
        else:               # 숫자가 아닐 경우
            if stack:       # 스택이 남아있으면
                postfix.append(stack.pop()) # 스택을 뽑아서 후위표기법 리스트에 push
                stack.append(x)     # stack에 연산자를 push
            else:           # 스택이 없을 경우엔 연산자만 추가
                stack.append(x)
    else:   # for문 순회가 끝났을 때 stack에 남아있으면 후위표기법에 추가
        if stack:
            postfix.append(stack.pop())

    # ------ 후위표기법을 불러와서 계산 ------ #
    stack, result = [], 0
    for x in postfix:
        if x.isnumeric():   # 1. 피연산자를 만나면 stack에 push
            stack.append(x)
        else:
            # 2. 연산자를 만나면 필요한만큼의 피연산자를 스택에서 pop해서 연산하고
            stack.append(int(stack.pop()) + int(stack.pop()))   # 연산 결과를 스택에 push

    # 3. 수식이 끝나면 스택을 pop하여 출력
    print(f'#{tc} {sum(stack)}')