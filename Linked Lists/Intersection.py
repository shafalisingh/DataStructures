class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head = None

def getIntersectionNode( headA, headB):
        curA, curB = headA, headB
        lenA, lenB = 0, 0
        while curA is not None:
            lenA += 1
            curA = curA.next
        while curB is not None:
            lenB += 1
            curB = curB.next
        curA, curB = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                curB = curB.next
        while curB is not None:
            if curA!=curB:
             curB = curB.next
             curA = curA.next
            elif curA==curB:
                return curA


if __name__ == '__main__':
    llist1=LinkedList()
    llist1.head=Node(3)
    llist1.head.next=Node(1)
    llist1.head.next.next=Node(5)
    llist1.head.next.next.next=Node(9)
    llist1.head.next.next.next.next=Node(7)
    llist1.head.next.next.next.next.next=Node(2)
    llist2=LinkedList()
    llist2.head=Node(4)
    llist2.head.next=Node(6)
    llist2.head.next.next=Node(7)
    llist2.head.next.next.next=Node(2)
    print getIntersectionNode(llist1.head,llist2.head)