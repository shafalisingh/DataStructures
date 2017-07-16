class Node:
    def __init__(self,data):
        self.next=None
        self.data=data
class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def intersection(self,list_1,list_2):
        list_3=[]

        temp_1=list_1.head
        temp_2=list_2.head
        while(temp_1):
            while(temp_2):
                if temp_1.data==temp_2.data:
                    list_3.append(temp_1.data)
                temp_2=temp_2.next
            temp_1=temp_1.next
            temp_2=list_2.head
        return list_3

if __name__ == '__main__':
    list_1=LinkedList()
    llist=LinkedList()
    list_1.push(6)
    list_1.push(4)
    list_1.push(3)
    list_1.push(2)
    list_1.push(1)

    list_2=LinkedList()
    list_2.push(9)
    list_2.push(8)
    list_2.push(6)
    list_2.push(4)
    list_2.push(2)
    my_intersect=llist.intersection(list_1,list_2)
    print(my_intersect)