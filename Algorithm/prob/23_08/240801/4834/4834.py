import sys

sys.stdin = open('input.txt')

def my_max(lst):
    max_v = lst[0]
    for x in lst:
        if max_v < x:
            max_v = x
    idx_lst = [idx for idx, value in enumerate(lst) if value == max_v]
    return [max_v, idx_lst]

def my_many(lst):
    many_v = lst[0]
    many_lst = [0] * 10
    for idx, value in enumerate(lst):
        many_lst[value] += 1
    return my_max(many_lst)[1]

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    if len(my_many(arr)) > 1:
        result = my_max(my_many(arr))[0]
        result_idx = arr.count(result)
    else:
        result = my_many(arr)[0]
        result_idx = arr.count(result)

    print(f'#{tc} {result} {result_idx}')