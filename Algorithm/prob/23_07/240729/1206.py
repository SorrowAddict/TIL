def lst_max(lst, i):
    max_value=lst[i-2]
    dx = [-2, -1, 1, 2]
    for j in dx:
        if max_value < lst[i+j]:
            max_value = lst[i+j]
    return max_value

def check_view(lst, i):
    if lst[i-1]<lst[i] and lst[i-2]<lst[i] and lst[i+1]<lst[i] and lst[i+2]<lst[i]:
        return lst[i]-lst_max(lst, i)
    else:
        return 0

for _ in range(1, 11):
    result = 0
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(2, N-2):
        result += check_view(arr, i)
    print(f'#{_} {result}')