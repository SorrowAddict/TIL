import sys

sys.stdin = open('input.txt')

icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

# Testcase 만큼 반복
for tc in range(1, 11):
    l = int(input())
    N = input()
    post_fix, stack = [], []

    # ------ 후위 표기식 변환 ------ #
    for x in N:
        if x.isnumeric():
            post_fix.append(x)
        else:
            if x == '(':
                stack.append(x)
            elif x == ')':
                while 1:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    elif stack[-1] != '(':
                        post_fix.append(stack.pop())
            else:
                while stack and icp[x] <= isp[stack[-1]]:
                    post_fix.append(stack.pop())
                stack.append(x)
    else:
        while stack:
            post_fix.append(stack.pop())
    # ------ 여기까지 ------ #

    # ------ 변환식 계산 ------ #
    stack = []
    for x in post_fix:
        if x.isnumeric():
            stack.append(int(x))
        else:
            if x == '*':
                stack.append(stack.pop()*stack.pop())
            elif x == '+':
                stack.append(stack.pop()+stack.pop())
            elif x == '/':
                stack.append(stack.pop(-2)//stack.pop(-1))
            elif x == '-':
                stack.append(stack.pop(-2)-stack.pop(-1))
    # ------ 여기까지 ------ #

    print(f'#{tc}', stack[-1])