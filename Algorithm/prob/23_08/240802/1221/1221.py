import sys

sys.stdin = open('input.txt')

def BubbleSort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    test_case, length = input().split()
    length = int(length)
    arr = list(map(str, input().split()))
    key = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
           "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

    # str을 int 타입으로 변환
    len_arr = 0
    for idx, x in enumerate(arr):
        arr[idx] = key[x]
        len_arr += 1

    # 버블 정렬 시행
    result = BubbleSort(arr, len_arr)

    # int 타입을 str로 변환
    for idx, x in enumerate(arr):
        result[idx] = list(key.keys())[x]

    print(f'#{tc}')
    print(*result)