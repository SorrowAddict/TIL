import sys

sys.stdin = open('input.txt')

# Testcase 수
T = 10

# Testcase 만큼 반복
for tc in range(1, T+1):
    N, word_list = map(str, list(input().split()))
    result = 0

    while 1:    # 반복문자가 없을때까지 반복
        sub_result = 0      # while문이 돌때마다 반복 카운트값을 0으로 지정
        check_list = []     # 반복문자가 없는 문자를 저장
        for x in word_list:
            if not check_list:  # 첫 문자 입력 예외처리
                check_list.append(x)
            else:               # 그 이후 입력부터는
                check_v = check_list.pop()  # pop()으로 뽑아서
                if x == check_v:            # 중복을 체크
                    sub_result += 1         # 중복이면 중복 count += 1
                else:
                    check_list.append(check_v)  # 반복이 아니면 pop한 글자를 넣고
                    check_list.append(x)        # x도 추가
        if sub_result != 0:         # 반복을 돌 때 반복 카운트가 있으면
            word_list = check_list          # 반복을 제외한 리스트를 word_list에 재지정
            result += sub_result    # 전체 결과값에 반복 카운트값 더하기
        else:
            break   # 반복을 돌 때 반복되는 문자가 없으면 while문을 break

    print(f'#{tc}', ''.join(word_list))   # 초기 N값의 길이값에서 result*2를 빼기