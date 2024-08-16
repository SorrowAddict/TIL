import sys

sys.stdin = open('input.txt')

T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = list(map(str, input().split()))

    # ------ 후위표기법을 불러와서 계산 ------ #
    stack = []
    for x in N:
        if x.isnumeric():   # 1. 피연산자를 만나면 stack에 push
            stack.append(x)
        else:
            # 2. 연산자를 만나면 필요한만큼의 피연산자를 스택에서 pop해서 연산하고
            # 연산 결과를 스택에 push
            try:    # 사칙연산 처리
                if x == '+':
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif x == '-':
                    stack.append(int(stack.pop(-2)) - int(stack.pop(-1)))
                elif x == '*':
                    stack.append(int(stack.pop()) * int(stack.pop()))
                elif x == '/':
                    stack.append(int(stack.pop(-2)) // int(stack.pop(-1)))
                elif x == '.':  # . 일때 stack에 숫자가 1개를 초과하면 에러
                    if len(stack) > 1:
                        print(f'#{tc} error')
                    else:
                        print(f'#{tc} {stack.pop()}')
            except:
                print(f'#{tc} error')
                break