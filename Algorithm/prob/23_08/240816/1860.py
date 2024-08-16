#1860. 진기의 최고급 붕어빵

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    check = [[]]

    arr.sort()
    if arr[0] < M:
        print(f'#{tc}', 'Impossible')
    else:
        max_q = arr[-1] // M
        check_arr = [[] for _ in range(max_q + 1)]
        for x in arr:
            check_arr[x // M].append(x % M)

        total_num = -K
        for x in check_arr:
            total_num += K
            total_num -= len(x)
            if total_num < 0:
                print(f'#{tc}', 'Impossible')
                break
        else:
            print(f'#{tc}', 'Possible')