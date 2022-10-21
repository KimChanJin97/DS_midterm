class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

    def __eq__(self, other):
        if not isinstance(other, Node):
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
        new_node = self.next_ = Node(node_new)

        if self.head is None:
            self.head = new_node
        else:
            temp_node = self.head
            self.head = new_node
            self.head.next = temp_node

    def add_tail(self, node_new):
        new_node = Node(node_new)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    def delete_tail(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None

    def delete_head(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp = None

    def insert_after(self, node, node_new):
        new_node = self.next_ = Node(node_new)

        temp = self.head
        num = 0
        while temp is node:
            temp = temp.next
            num += 1

        temp = self.head
        if num == 0:
            new_node.next = self.head.next
            self.head.next = new_node
        else:
            for _ in range(num):
                if temp is not None:
                    temp = temp.next
            if temp is not None:
                new_node.next = temp.next
                temp.next = new_node


    def insert_before(self, node, node_new):
        new_node = self.next_ = Node(node_new)

        temp = self.head
        num = 0
        while temp is node:
            temp = temp.next
            num += 1

        temp = self.head
        if num == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(num):
                if temp is not None:
                    temp = temp.next
            if temp is not None:
                temp.next = new_node
                new_node.next = temp.next.next

    def is_empty(self):
        return not self.head

    def __str__(self):
        result = "["
        iterator = self.head

        while iterator is not None:
            result += str(iterator)
            iterator = iterator.next

            if iterator is not None:
                result += ", "

        result += "]"
        return result


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