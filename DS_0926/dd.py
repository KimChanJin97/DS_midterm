#doubly linekd list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_head(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_before(self, data, before_data):
        if self.head is None:
            return
        new_node = Node(data)
        cur = self.head
        while cur is not None:
            if cur.data == before_data:
                new_node.prev = cur.prev
                new_node.next = cur
                cur.prev.next = new_node
                cur.prev = new_node
                return
            cur = cur.next