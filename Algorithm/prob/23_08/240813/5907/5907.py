import sys

sys.stdin = open('input.txt')

from collections import deque

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = deque(list(map(int, input().split())))

    for _ in range(M):
        arr.append(arr.popleft())

    print(f'#{tc}', arr[0])