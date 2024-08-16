icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

N = input()
post_fix, stack = [], []

# ------ 후위 표기식 변환 ------ #
for x in N:
    if x.isalpha():
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

print(''.join(post_fix))