#Remove duplicates without buffer
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def deleteDups2(linkedlist):
        currNode = linkedlist.head
        while currNode != None:
            runner = currNode
            while runner.next != None:
                if runner.next.val == currNode.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            currNode = currNode.next

    def printList(self):
        temp = self.head
        while (temp):
            print temp.val,
            temp = temp.next

if __name__ == '__main__':
    llist=LinkedList()
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)
    four=Node(2)
    five=Node(4)
#    print llist
    llist.head.next = second;
    second.next = third;
    third.next=four;
    four.next=five;
    llist.deleteDups2()
    llist.printList()