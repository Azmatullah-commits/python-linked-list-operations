# Insert a New Node After a Given Value

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_after_value(self, key, new_value):
        temp = self.head

        while temp is not None:
            if temp.data == key:
                new_node = Node(new_value)
                new_node.next = temp.next
                temp.next = new_node
                return

            temp = temp.next

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Creating Linked List
mylist = LinkedList()
mylist.head = Node(10)
mylist.head.next = Node(20)
mylist.head.next.next = Node(30)

# Inserting 25 after 20
mylist.insert_after_value(20, 25)

# Display Result
mylist.display()