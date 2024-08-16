import sys

sys.stdin = open('input.txt')

def exponent(idx, exp):
    if exp < 1:
        return 1
    return idx * exponent(idx, exp-1)

# Testcase 수
T = 10

# Testcase 만큼 반복
for _ in range(1, T+1):
    tc = int(input())
    N, M = map(int, input().split())

    result = exponent(N, M)

    print(f'#{tc}', result)