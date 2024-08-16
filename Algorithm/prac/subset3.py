def f(i, k, s, t):  # i원소, k 집합의 크기, s i-1까지 고려된 합, t 목표
    global cnt
    global fcnt
    fcnt+=1
    # if i == k:  # 모든 원소 고려
    #     if s == t:
    #         print(bit)
    #         cnt += 1
    #     return
    # ----- 가지치기 ----- #
    if s > t:   # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif s == t:    #남은 원소를 고려할 필요가 없는 경우
        cnt += 1
        return
    elif i == k:    # 모든 원소 고려
        return
    # ----- 까지 ----- #
    else:
        bit[i] = 1
        f(i+1, k, s +A[i], t)   # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)         # A[i] 미포함

N = 10
A = [i for i in range(1, N+1)]

key = 10
cnt = 0         # 합이 key와 같은 부분 집합의 수
bit = [0] * N
fcnt = 0
f(0, N, 0, key)
print(cnt)