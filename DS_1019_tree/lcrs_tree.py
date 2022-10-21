from stacks import Stack

class Tree:
    def __init__(self):
        self.root = None

    def build(self, sexpr):
        stack = Stack()
        count = 0
        num_count = 0
        check = 0
        child_check = 0

        for i in sexpr:
            if i == "(":
                count += 1
                check = 0
                child_check = 1
            elif i == ")":
                if check == 1:
                    num = 1
                else:
                    num = num_count - count + 1
                while num > 0:
                    num -= 1
                    stack.pop()
                    num_count -= 1

                count -= 1
                print(") :", stack, count, num_count, check)


            else:
                num_count += 1
                check += 1
                i = self.TreeNode(i)
                print(i, "num : ", stack, count, num_count, check, child_check)

                if count == 1:
                    self.root = i
                elif child_check == 1:
                    a = stack.peek()
                    a.left_child = i
                    print("child")
                    child_check = 0
                else:
                    a = stack.peek()
                    a.right_sibling = i
                    print("right")
                stack.push(i)


    class TreeNode:
        def __init__(self, elem):
            self.elem = elem
            self.left_child = None
            self.right_sibling = None

        def __repr__(self):
            return str(self)

        def __str__(self):
            return f"{self.elem}"

if __name__ == "__main__":

    sexpr = "( A ( B ( E ( K L ) F ) C ( G ) D ( H ( M ) I J ) ) )"
    sexpr = sexpr.split()

    tree = Tree()
    tree.build(sexpr)
    root = tree.root
    print(root)
    b = root.left_child
    print(b)
    e = b.left_child
    print(e)
    k = e.left_child
    print(k)
    l = k.right_sibling
    print(l)
    f = e.right_sibling
    print(f)
    c = b.right_sibling
    print(c)
    d = c.right_sibling
    print(d)
    g = c.left_child
    print(g)
    h = d.left_child
    print(h)
    i = h.right_sibling
    print(i)
    j = i.right_sibling
    print(j)