class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

    def __eq__(self, other):
        if not isinstance(other, None):
            return False

        if self is other or self.item == other.item:
            return True

        return False

    def __str__(self):
        return f"{self.item}"


class SinglyLinkedList:
    def __init__(self):
        self.head = self.next_ = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_ is not None:
            temp = self.next_
            self.next_ = self.next_.next
            return temp
        else:
            raise StopIteration

    def add_head(self, node_new):
        self.next_ = node_new

        if self.head is None:
            self.head = node_new
        else:
            temp = self.head
            self.head = node_new
            self.head.next = temp

    def add_tail(self, node_new):
        if self.head is None:
            self.head = node_new
        else:
            tail = self.head
            while tail.next:
                tail = tail.next

            tail.next = node_new

    def delete_tail(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next != None:
                    temp = temp.next
                temp.next = None

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next

    def insert_after(self, node, node_new):
        self.next_ = node_new

        temp = self.head
        cnt = 0
        while temp is node:
            temp = temp.next
            cnt += 1
        temp = self.head
        if cnt == 0:
            self.next_.next = self.head.next
            self.head.next = self.next_
        else:
            for _ in range(cnt):
                if temp is not None:
                    temp = temp.next
            if temp is not None:
                self.next_.next = temp.next
                temp.next = self.next_

    def insert_before(self, node, node_new):
        self.next_ = node_new

        temp = self.head
        cnt = 0
        while temp is node:
            temp = temp.next
            cnt += 1
        temp = self.head
        if cnt == 0:
            self.next_.next = self.head
            self.head = self.next_
        else:
            for _ in range(cnt):
                if temp is not None:
                    temp = temp.next
            if temp is not None:
                temp.next = self.next_
                self.next_.next = temp.next.next

    def delete(self, node):
        temp = self.head

        if temp is not None:
            if temp.item == node.item:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.item == node.item:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def __str__(self):
        res = []
        iterator = self.head

        while iterator:
            res.append(iterator.item)
            iterator = iterator.next

        return f"{res}"


if __name__ == "__main__":
    list_ = SinglyLinkedList()
    list_.add_head(Node(50))
    list_.add_tail(Node(100))
    list_.add_tail(Node(150))
    print("1", list_)

    list_.delete_head()
    print("2", list_)
    list_.delete_tail()
    print("3", list_)
    list_.delete_head()
    print("4", list_)

    list_.add_tail(Node(150))
    list_.insert_before(Node(150), Node(999))
    print("5", list_)

    list_.add_head(Node(50))
    list_.add_tail(Node(100))
    print("6", list_)

    for i in list_:
        print("Element:", i)

    list_.add_tail(Node(700))
    print("7", list_)

    list_.insert_after(Node(50), Node(250))
    print("8", list_)

    list_.insert_before(Node(50), Node(750))
    print("9", list_)

    for i in list_:
        print("Element:", i)

    list_.delete(Node(999))
    print("10 delete Node(999)", list_)