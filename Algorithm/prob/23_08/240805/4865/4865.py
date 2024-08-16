import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = input()
    M = list(input())
    max_v = 0
    for x in N:
        if max_v < M.count(x):
            max_v = M.count(x)
    result = 0

    print(f'#{tc}', max_v)