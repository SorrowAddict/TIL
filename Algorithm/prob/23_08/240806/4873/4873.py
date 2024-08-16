import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T + 1):
    N = list(input())
    stack = []

    # 문자열 조회
    for x in N:
        if not stack:       # 첫 입력이면 stack에 push
            stack.append(x)
            continue
        if stack[-1] != x:  # stack의 최근 인덱스가 일치하지 않으면 push
            stack.append(x)
        else:               # 일치하면 pop
            stack.pop()

    print(f'#{tc}', len(stack))