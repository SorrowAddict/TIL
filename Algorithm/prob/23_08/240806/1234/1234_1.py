import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, word_list = map(str, list(input().split()))
    stack = []

    for x in word_list:
        if not stack:
            stack.append(x)
        elif x == stack[-1]:
            stack.pop()
        else:
            stack.append(x)

    print(f'#{tc}', ''.join(stack))