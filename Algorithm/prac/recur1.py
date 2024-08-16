def f(n):
    global cnt
    cnt += 1
    if n==0:  # 배열을 벗어난 경우
        return
    else:
        f(n-1)

cnt = 0
f(1000)
print(cnt)