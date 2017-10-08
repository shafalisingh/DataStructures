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

    def is_palindrome(ll):
        fast = slow = ll.head
        stack = []

        while fast and fast.next:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while slow:
            top = stack.pop()

            if top != slow.data:
                return False

            slow = slow.next

        return True
if __name__ == '__main__':
    llist=LinkedList()
    llist.head=Node('1')
    llist.head.next=Node('2')
    llist.head.next.next=Node('3')
    llist.head.next.next.next=Node('2')
    llist.head.next.next.next.next=Node('1')
    #llist.head.next.next.next.next.next=Node('1')


    print llist.is_palindrome()