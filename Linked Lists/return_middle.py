class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print temp.data,
            temp = temp.next
    def middle(list1):
        slow,fast=list1.head,list1.head
        while fast and fast.next is not None :
            slow=slow.next
            fast=fast.next.next
        return slow.data



llist = LinkedList()
llist.push(2)
llist.push(3)
#llist.push('C')
llist.push(4)
llist.push(5)

# Create a loop for testing
#llist.head.next.next.next.next.next = llist.head
print llist.middle()
