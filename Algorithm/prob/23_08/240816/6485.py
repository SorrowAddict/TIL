'''
1
2
1 3
2 5
5
1
2
3
4
5

'''

# # 6485. 삼성시의 버스 노선
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     counts = [0] * 5001 # 5000번 정류장까지
#     # N개의 노선 정보를 모두 읽어놓고 처리 or 읽을 때마다 처리
#     for _ in range(N):      # 읽을 때마다 처리
#         A, B = map(int, input().split())    # Ai -> Bi 버스 노선의 시점 Ai와 종점 Bi, Ai<=Bi
#         for i in range(A, B+1):     # 1 <= Ai <= Bi <= 5,000
#             counts[i] += 1
#
#     P = int(input())    # 노선수를 출력할 P개의 버스 정류장
#     # 모두 읽어놓고 처리
#     bus_stop = [int(input()) for _ in range(P)]
#     print(f'#{tc}', end= ' ')
#     for j in bus_stop:  # 노선수를 출력할 정류장 번호
#         print(counts[j], end= ' ')
#     print()

# --------------------------------------------------------- #

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 5001
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            counts[i] += 1

    P = int(input())
    lst = [int(input()) for _ in range(P)]

    print(f'#{tc}', end= ' ')
    for x in lst:
        print(counts[x], end= ' ')
    print()