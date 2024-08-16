import sys

sys.stdin = open('input.txt')

def bubble_sort(lst):
    for i in range(len(lst), 0, -1):
        for j in range(i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    check = [[]]

    bubble_sort(arr)
    if arr[0] < M:
        print(f'#{tc}', 'Impossible')
    else:
        # while remain != 0:
        max_q = arr[-1]//M
        check_arr = [[] for _ in range(max_q+1)]
        # print(max_q, len(check_arr))
        for x in arr:
            check_arr[x//M].append(x%M)
        # print(check_arr)

        total_num = -K
        for x in check_arr:
            total_num += K
            total_num -= len(x)
            if total_num < 0:
                print(f'#{tc}', 'Impossible')
                break
        else:
            print(f'#{tc}', 'Possible')