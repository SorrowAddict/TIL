def f(i, N, s, t):  # i 배열의 시작 인덱스값, N 집합의 크기, s i-1 까지 고려합, t 타겟
    global cnt
    # ----- 가지치기 ----- #
    if s == t:       # 부분 합이 타겟과 일치하면 cnt+=1 증가 하고 패스
        cnt += 1
        return
    elif s > t:      # 부분 합이 높을 경우에 패스
        return
    elif i == N:     # 전체 탐색 했을 경우 패스
        return
    # ----- 까지 ------ #
    else:            # i가 1, 0인 경우의 i+1 갈래의 재귀 함수 실행
        bit[i] = 1
        f(i+1, N, s+A[i], t)
        bit[i] = 0
        f(i+1, N, s, t)
    return cnt       # 최종 결과값 출력

N = 10      # 집합의 크기
A = [i for i in range(1, N+1)]  # 1~10 까지의 배열
key = 10    # 찾을 값
cnt = 0     # 찾을 값이 나오는 부분 집합의 수
bit = [0] * N   # 부분 집합으로 뽑아 쓸건지 의사결정 리스트

print(f'#1', f(0, N, 0, key))