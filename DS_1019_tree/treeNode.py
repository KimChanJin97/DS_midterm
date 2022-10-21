class TreeNode:
    def __init__(self, elem):
        self.elem = elem
        self.left_child = None
        self.right_sibling = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.elem}"


# degree : 자식노드 개수
# depth : root node에서 나까지
# height : 나에서 leaf node까지

# degree of tree : 최대 자식노드 개수
# size of tree : tree를 구성하고 있는 node 개수
# height of tree : 최대 나에서 leaf node까지
# leaf node : degree가 0인 node (자식이 없는 node)
# internal node : degree가 0 이상인 node (자식을 가진 node)

# parent : 부모
# child : 자식
# sibling : 형제
# ancestor : root node까지의 path에 존재하는 node들

# descendent : 자손(leaf node까지), 자식과 헷갈리지 말 것
# level : node가 존재하는 층

# degree of tree를 기준으로 자리 마련하면 메모리 낭비
#

