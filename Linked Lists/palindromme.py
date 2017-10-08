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
    def palinLL(self):
        curr=self.head
        list=[]
        while curr:
            list.append(curr.data)
            curr=curr.next
        if list==list[::-1]:
            print 'It is a Palindrome'
        else:
            print 'It is not a Palindrome'
if __name__ == '__main__':
    llist=LinkedList()
    llist.head=Node('M')
    llist.head.next=Node('A')
    llist.head.next.next=Node('D')
    llist.head.next.next.next=Node('A')
    llist.head.next.next.next.next=Node('M')

    llist.palinLL()
    #llist.printList()