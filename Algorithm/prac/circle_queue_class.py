# 원형 큐
class cQueue:
    def __init__(self, size):
        self.front = 0
        self.rear = 0
        self.cQ = [None] * size
        self.size = size

    def is_full(self):
        return (self.rear + 1) % self.size == self.front


    def is_empty(self):
        return self.rear == self.front


    def enQ(self, value):
        if self.is_full():
            print('Q is Full')
        else:
            self.rear = (self.rear + 1) % self.size
            self.cQ[self.rear] = value

    def deQ(self):
        if self.is_empty():
            print('Q is Empty')
        else:
            self.front = (self.front + 1) % self.size
            temp = self.cQ[self.front]
            self.cQ[self.front] = None
            return temp

    # q_peek : 곧 삭제될 원소 (실제 삭제하지는 않음)
    def q_peek(self):
        if self.is_empty():
            print('Q is empty')
        else:
            return self.cQ[(self.front + 1) % self.size]


# q를 생성해서 사용해보자!
q = cQueue(4)
# 최초 상태
print(q.rear, q.front)

# A 추가, B 추가
q.enQ('A')
q.enQ('B')

print(q.rear, q.front)
print(q.q_peek())


print(q.deQ(), q.front, q.cQ)
q.enQ('C')
q.enQ('D')

print(q.cQ, q.is_full())
q.enQ('E')

# print(q.deQ(), q.deQ(), q.front, q.is_empty())