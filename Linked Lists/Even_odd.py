#Given a Linked List of integers, write a function to modify the linked list such that all even numbers appear before all the
#  odd numbers in the modified linked list. Also, keep the order of even and odd numbers same.
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

    def even_odd(self):
        temp=self.head
        list_1=[]
        list_2=[]
        while temp:
            if temp.data%2==0:
                list_1.append(temp.data)
            else:
                list_2.append(temp.data)
            temp=temp.next
        list_3=[]
        for elem in list_1:
            list_3.append(elem)
        for elem in list_2:
            list_3.append(elem)
        return list_3

llist=LinkedList()
list_1=LinkedList()
list_2=LinkedList()
llist.push(8)
llist.push(1)
llist.push(5)
llist.push(6)
llist.push(3)
my_list=llist.even_odd()
print(my_list)