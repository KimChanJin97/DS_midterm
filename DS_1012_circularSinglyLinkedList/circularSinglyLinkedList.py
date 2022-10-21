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

class CircularSinglyLinkedList:
    def __init__(self):
        self.tail = None

    def add_head(self, node_new):
        new_node = Node(node_new)

        if self.tail is None: # CSLL객체의 tail이 존재하지 않다면
            self.tail = new_node # 새 Node객체가 CSLL객체의 tail이 된다
            new_node.next = new_node # 새 Node객체의 next가 새 Node객체로 순환 (내가 나로 순환)
        else: # CSLL객체의 tail이 존재한다면
            new_node.next = self.tail.next # 새 Node객체의 next가 CSLL객체의 tail의 next(첫번째 Node)로 이어짐
            # circular에서 tail의 next가 head
            self.tail.next = new_node # CSLL객체의 tail의 next가 새 Node객체로 이어짐

    def add_tail(self, node_new):
        new_node = Node(node_new)

        if self.tail is None: # CSLL객체의 tail이 존재하지 않다면
            self.tail = new_node # 새 Node객체가 CSLL객체의 tail이 된다
            new_node.next = new_node # 새 Node객체의 next가 새 Node객체로 순환 (내가 나로 순환)
        else: # CSLL객체의 tail이 존재한다면
            new_node.next = self.tail.next # 새 Node객체의 next가 CSLL객체의 tail의 next(첫번째 Node)로 이어짐
            self.tail.next = new_node # CSLL객체의 tail의 next가 새 Node객체로 이어짐
            self.tail = new_node # 새 Node객체가 이제 tail

    def delete_tail(self):
        if self.tail.next is not None: # CSLL객체의 tail의 next가 존재한다면
            if self.tail is self.tail.next: # CSLL객체의 tail이 CSLL객체의 tail의 next라면 (내가 나로 순환하는 상황이라면)
                self.tail = None # tail을 None처리 (tail 삭제)
            else: # CSLL객체의 tail이 CSLL객체의 tail의 next가 아니라면 (내가 나로 순환하는 상황이 아니라면)
                temp = self.tail # temp에 CSLL객체의 tail을 저장
                while temp.next is not self.tail: # temp의 next가 CSLL객체의 tail이기 전까지
                    temp = temp.next # temp.next 가 temp (tail 직전에 도착할 때까지 옆으로 한칸씩 이동)
                    # temp는 tail 직전 Node가 된다
                temp.next = self.tail.next # tail 직전 Node의 next를 CSLL객체의 첫번째 Node가 된다 (원래 CSLL객체의 tail 배제)
                self.tail = temp # temp가 CSLL객체의 tail이 된다

    def delete_head(self):
        if self.tail.next is not None: # CSLL객체의 tail의 next가 존재한다면
            if self.tail.next is self.tail: # CSLL객체의 tail의 next가 CSLL객체의 tail이라면 (내가 나로 순환하는 상황이라면)
                self.tail = None # tail을 None처리 (tail 삭제, tail이 곧 head인 상황이니깐)
            else: # CSLL객체의 tail의 next가 CSLL객체의 tail이 아니라면 (내가 나로 순환하는 상황이 아니라면)
                temp = self.tail.next # temp에 CSLL객체의 첫번째 Node(head)를 저장

                while temp.next is not self.tail.next: # temp의 next가 CSLL객체의 첫번째 Node(head)이기 전까지
                    temp = temp.next # temp.next가 temp (tail에 도착할 때까지 옆으로 한칸씩 이동)
                    # temp는 tail이 된다
                self.tail.next = self.tail.next.next # 첫번째 Node는 두번째 Node가 된다 (원래 CSLL객체의 head 배제)
                temp.next = self.tail.next # tail의 next가 두번째 Node가 된다

    def insert_after(self, node, node_new):
        new_node = Node(node_new)

        temp = self.tail # temp에 tail 저장

        while str(temp.next) != str(node): # tail의 next가 node(인자값)가 아닐 때까지
            temp = temp.next # tail.next가 temp (node 직전에 도착할 때까지 옆으로 한칸씩 이동)
            # temp는 node(인자값) 직전이 된다
        if temp.next is self.tail: # node(인자값)의 next가 tail이라면 (존재하는 Node가 2개라면)
            new_node.next = self.tail.next # new_node의 next가 첫번째 Node가 된다
            self.tail.next = new_node # 첫번째 Node는 new_node가 된다
            self.tail = new_node #
        else: # node(인자값)의 next가 tail이 아니라면
            new_node.next = temp.next.next
            temp.next.next = new_node

    def insert_before(self, node, node_new):
        new_node = Node(node_new)

        temp = self.tail

        while str(temp.next) != str(node):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def delete(self, node):
        temp = self.tail.next
        temp_prev = self.tail
        while temp is not node:
            temp = temp.next
            temp_prev = temp_prev.next

        temp_prev.next = temp.next

    def __str__(self):
        result = "["

        if self.tail is not None:
            iterator = self.tail.next

            if iterator is not None:
                result += str(iterator)
                if self.tail is not self.tail.next:
                    result += ", "
                iterator = iterator.next

            while iterator is not self.tail.next:
                result += str(iterator)
                iterator = iterator.next

                if iterator is not self.tail.next:
                    result += ", "

        result += "]"

        return result

list_ = CircularSinglyLinkedList()
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

list_.add_tail(Node(700))
print("7", list_)

list_.insert_after(Node(50), Node(250))
print("8", list_)

list_.insert_before(Node(50), Node(750))
print("9", list_)