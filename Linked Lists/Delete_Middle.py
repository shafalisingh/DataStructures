class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next

    def deleteNode(self, node):
        if node.next != None:
            node.data = node.next.data
            node.next = node.next.next

            # if the given node is the last one, no way to delete it.
        # Here we set the last one's value to None
        else:
            node.value = None
if __name__ == '__main__':
    llist=LinkedList()
    llist.head=Node(11)
    llist.head.next=Node(12)
    llist.head.next.next=Node(13)
    llist.head.next.next.next=Node(14)
    llist.head.next.next.next.next=Node(15)
    node=llist.head.next
    llist.deleteNode(node)
    llist.printList()




