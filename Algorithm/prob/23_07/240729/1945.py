T = int(input())

for i in range(1, T+1):
    N = int(input())
    num_lst = [2, 3, 5, 7, 11]
    arr = []
    for j in num_lst:
        cnt = 0
        while 1:
            if N == 1:
                break
            elif N % j == 0:
                cnt += 1
                N = N//j
            else:
                break
        arr.append(cnt)
    arr = list(map(str, arr))
    print(f"#{i} {' '.join(arr)}")