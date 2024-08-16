# 선형 Q 인 경우
class Queue:
    # front, rear 관리를 하려면 생성할 때 size 만큼 queue 를 생성해야 함
    def __init__(self, size):     # createQueue(size)
        self.front = -1
        self.rear = -1
        self.Q = [None] * size
        self.size = size            # Q의 길이

    def enQ(self, value):
        # Q가 가득차 있을 때는 더이상 추가 불가능
        if self.is_full():  # 포화 상태 확인
            print('Q is Full!!!')
        else:
            self.rear += 1              # rear 1 증가
            self.Q[self.rear] = value   # 증가한 위치에 값을 추가

    def deQ(self):
        # Q가 비어있다면 더이상 deQ 할 수 없음
        if self.is_empty():
            print('Q is Empty!!!')
        else:
            self.front += 1
            temp = self.Q[self.front]   # 값을 실제로 지우기 위해 임시 저장
            self.Q[self.front] = None   # front 위치의 값을 지움
            return temp

    def is_full(self):
        return self.rear == self.size - 1

    def is_empty(self):
        return self.front == self.rear

    # q_peek : 곧 삭제될 원소 (실제 삭제하지는 않음)
    def q_peek(self):
        if self.is_empty():
            print('Q is empty')
        else:
            return self.Q[self.front + 1]


# q를 생성해서 사용해보자!
q = Queue(3)
# 최초 상태
print(q.rear, q.front)

# A 추가, B 추가
q.enQ('A')
q.enQ('B')

print(q.rear, q.front)
print(q.q_peek())


print(q.deQ(), q.front, q.Q)
q.enQ('C')

print(q.Q, q.is_full())
q.enQ('D')
print(q.deQ(), q.deQ(), q.front, q.is_empty())
















