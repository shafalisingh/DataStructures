class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp = self.head
        while (temp):
            print temp.val,
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def  kth(self,n):
        curr=self.head
        follow=self.head
        for i in range(n-1):
            curr=curr.next
        while curr.next!=None:
            follow=follow.next
            curr=curr.next
        print follow.val



if __name__ == '__main__':
    llist=LinkedList()
    llist.head=Node(11)
    llist.head.next=Node(12)
    llist.head.next.next=Node(13)
    llist.head.next.next.next=Node(14)
    llist.head.next.next.next.next=Node(15)
    llist.kth(2)

