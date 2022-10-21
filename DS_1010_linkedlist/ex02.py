class Item:
    def __init__(self, data):
        self.data = data
        self.link = None

    def __str__(self):
        return f"Item: {self.data}"

def explore(i):
    while i is not None:
        print(f"({i})", end="->")
        i = i.link
    print("\b\b")

item0 = Item(0)
item1 = Item(1)
item2 = Item(2)

item0.link = item1
item1.link = item2

explore(item0)