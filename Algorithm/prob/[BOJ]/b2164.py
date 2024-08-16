from collections import deque

N = deque(i+1 for i in range(int(input())))

def card_game(lst):
    while len(lst) > 1:
        lst.popleft()
        if len(lst) == 1:
            return lst[0]
        lst.append(lst.popleft())
    return lst[0]

print(card_game(N))