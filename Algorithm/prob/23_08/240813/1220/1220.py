import sys

sys.stdin = open('input.txt')

# Testcase 만큼 반복
for tc in range(1, 11):
    l = int(input())  # 이 값은 항상 100
    arr = [input().split() for _ in range(l)]
    result = 0

    for lst in zip(*arr):
        temp = ''.join(lst)
        temp = temp.replace('0', '')
        result += temp.count('12')

    print(f'#{tc}', result)