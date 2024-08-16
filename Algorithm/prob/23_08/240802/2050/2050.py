import sys

sys.stdin = open('input.txt')

# word 입력
word = input()

for x in word:
    print(ord(x)-64, end=' ')