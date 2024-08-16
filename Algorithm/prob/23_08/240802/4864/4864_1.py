import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = input(), input()
    result = 0
    if N in M:
        result = 1

    print(f'#{tc}', result)