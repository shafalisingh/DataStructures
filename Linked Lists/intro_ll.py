# linked list with 3 nodes
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

if __name__ == '__main__':
    llist=LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)/
    four=Node(2)
    five=Node(4)
#    print llist
    llist.head.next = second;
    second.next = third;
    third.next=four;
    four.next=five;

    llist.printList()