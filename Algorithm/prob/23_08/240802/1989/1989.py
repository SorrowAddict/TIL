import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    word = input()
    if word == word[::-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')