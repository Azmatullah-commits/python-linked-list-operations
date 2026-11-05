# Delete Duplicate Values from Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def delete_duplicates(self):
        temp = self.head

        while temp is not None:
            check = temp

            while check.next is not None:
                if check.next.data == temp.data:
                    check.next = check.next.next
                else:
                    check = check.next

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
mylist.head.next.next = Node(10)
mylist.head.next.next.next = Node(30)
mylist.head.next.next.next.next = Node(20)

# Removing Duplicates
mylist.delete_duplicates()

# Display Result
mylist.display()