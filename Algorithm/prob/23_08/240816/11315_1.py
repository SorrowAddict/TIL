# 11315. 오목 판정

di = [0, 1, 1,  1]
dj = [1, 1, 0, -1]
def check_dup(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='o':
                for k in range(4):
                    for l in range(1, 5):
                        ni, nj = i+di[k]*l, j+dj[k]*l
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj]=='o':
                            pass
                        else: break
                    else:
                        return 'YES'
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]

    print(f'#{tc}', check_dup(N))