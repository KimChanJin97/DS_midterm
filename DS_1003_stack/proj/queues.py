from proj.array import Array

class Queue:
    CAPACITY = 10

    def __init__(self, capacity=CAPACITY):
        self.arr = Array(capacity)
        self.capacity = capacity
        self.front = self.rear = -1 # 처음 queue 비어있다고 가정

    def is_full(self):
        return self.rear >= self.capacity - 1

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def enqueue(self, elem): # [rear] 넣고 +1
        if self.is_full():
            raise Exception("queue is full")
        self.rear += 1
        self.arr[self.rear] = elem

    def dequeue(self): # [front] 빼고 +1
        if self.is_empty():
            raise Exception("queue is empty")
        # 필요하다면 None 설정
        self.arr[self.front] = None
        if self.front == self.rear and self.front != -1:
            self.front = self.rear = -1
        else:
            self.front += 1

    def peek(self):
        if self.is_empty():
            raise Exception("queue is empty")
        return self.arr[self.front]

    def __len__(self): # queue의 실제 element 갯수
        # return self.capacity - self.arr.items.count(None)
        return 0 if self.is_empty() else self.rear - self.front + 1

    def __iter__(self):
        if self.is_empty():
            return
        pos = self.front
        while pos <= self.rear:
            yield self.arr[pos]
            pos += 1

    def __str__(self):
        return str(self.arr)