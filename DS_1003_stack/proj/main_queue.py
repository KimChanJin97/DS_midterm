from proj.queues import Queue

if __name__ == "__main__":
    N = 4
    queue = Queue(N)
    print(queue.is_empty())

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    print(len(queue), queue)
    queue.enqueue(4)
    print(len(queue), queue)