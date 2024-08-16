import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
S = int(input())
op = [1, 0]
for _ in range(S):
    sex, num = map(int, input().split())

    # 남자일 경우
    if sex == 1:
        for i in range(1, N//num+1):
            lst[num*i-1] = op[lst[num*i-1]]

    # 여자일 경우
    elif sex == 2:
        stack = [num-1]
        for i in range(1, 51):
            if 0<=num-i-1<N and 0<=num+i-1<N:
                if lst[num-1-i] == lst[num-1+i]:
                    stack.append(num-1-i)
                    stack.append(num-1+i)
                else:
                    break
            else:
                break
        for x in stack:
            lst[x] = op[lst[x]]

# 20개씩 묶어서 출력
for i in range(0, len(lst), 20):
    sublist = lst[i:i + 20]
    print(*sublist)