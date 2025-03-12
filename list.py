class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None

    def insert (self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last =self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_recursion(self, node):
        if node is None:
            return
        print (node.data)
        self.print_recursion(node.next)

    def strat_recursion_travesal(self):
        self.print_recursion(self.head)

list = Linklist()
list.insert(11)
list.insert(12)
list.insert(13)
list.insert(14)
list.insert(15)



print("Link List")
list.strat_recursion_travesal()