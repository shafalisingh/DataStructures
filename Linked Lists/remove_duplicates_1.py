#Remove duplicates with buffer
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
    def dups(List):
        if List.head!=None:
            curr=List.head
            dic={curr.val:1}
            while curr.next!= None:
                if curr.next.val in dic:
                    curr.next=curr.next.next
                else:
                    dic[curr.next.val]=1
                    curr=curr.next
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