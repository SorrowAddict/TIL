import sys

sys.stdin = open('input.txt')

def my_max(lst):
    global max_idx
    max_v = lst[0]
    for idx, x in enumerate(lst):
        if max_v <= x:
            max_v = x
            max_idx = idx
    return [max_v, max_idx]

def my_min(lst):
    min_v = lst[0]
    for idx, x in enumerate(lst):
        if min_v >= x:
            min_v = x
            min_idx = idx
    return [min_v, min_idx]

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):
    dump_tri = int(input())
    arr = list(map(int, input().split()))

    while dump_tri > 0:
        arr[my_max(arr)[1]] -= 1
        arr[my_min(arr)[1]] += 1
        dump_tri -= 1

    print(f'#{tc} {my_max(arr)[0] - my_min(arr)[0]}')