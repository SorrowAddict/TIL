import sys

sys.stdin = open('input.txt')

def recur(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return recur(N-10) + 2 * recur(N-20)

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}', recur(N))