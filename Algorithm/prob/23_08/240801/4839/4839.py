import sys

sys.stdin = open('input.txt')

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    arr = [i for i in range(1, P+1)]

    # 이진 탐색 진행
    def binarySearch(a, N, key):
        cnt = 0
        start = 1
        end = N
        while start <= end:
            middle = int((start+end)/2)
            cnt += 1
            if a[middle-1] == key:  # 검색 성공
                break
            elif a[middle-1] > key:
                end = middle - 1
            else:
                start = middle + 1
        return cnt

    X, Y = binarySearch(arr, P, A), binarySearch(arr, P, B)
    if X == Y:
        result = 0
    elif X < Y:
        result = 'A'
    else:
        result = 'B'

    print(f'#{tc} {result}')