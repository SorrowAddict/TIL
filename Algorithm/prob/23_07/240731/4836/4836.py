import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    cnt = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for j in range(r1, r2+1):
            for k in range(c1, c2+1):
                if color == 1 and arr[j][k] == 0:
                    arr[j][k] = color
                elif color == 1 and arr[j][k] == 2:
                    arr[j][k] = 9
                    cnt += 1
                elif color == 2 and arr[j][k] == 0:
                    arr[j][k] = color
                elif color == 2 and arr[j][k] == 1:
                    arr[j][k] = 9
                    cnt += 1
    print(f'#{tc} {cnt}')