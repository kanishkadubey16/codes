




    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_list = LinkedList()
my_list.insert_at_end(10)
my_list.insert_at_end(20)
my_list.insert_at_end(30)
my_list.print_list()

# Example Test
arr = [1, 3, 2, 4, 5]
head = createLinkedList(arr)

M = 3
K = 2

head = addElement(head, M, K)
print("After inserting at position", M, ":")
printList(head)






# thinkl for the edge case
