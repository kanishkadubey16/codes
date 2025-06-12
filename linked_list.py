'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
def merge(L1, L2):
    if L1 == None:
        return L2
    if L2 == None:
        return L1 
    temp = L1
    while temp.next != None:
        temp = temp.next 
    temp.next = L2
    return L1
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                break 
        if slow != fast:
            return True 
        slow = head 
        if slow == fast:
            while fast.next != slow:
                fast = fast.next 
        else:
            while slow.next != fast.next:
                slow = slow.next 
                fast = fast.next 
        fast.next = None 
        return True

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        slow = head 
        fast = head 
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                return True 
        return False

class Solution:
    def reverseList(self, head):
        prev = None 
        cur = head 
        while cur:
            next_node = cur.next 
            cur.next = prev 
            prev = cur 
            cur = next_node 
        return prev


class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None
        map = {}
        cur = head 
        while cur:
            map[cur] = Node(cur.data)
            cur = cur.next 
        cur = head 
        while cur:
            map[cur].next = map.get(cur.next)
            map[cur].random = map.get(cur.random)
            cur = cur.next 
        return map[head]
            







'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

'''
def make_circular(head):
    # take cur to last_node
    cur = head
    while cur.next != None:
        cur = cur.next 
    # make last node next ppoint to head
    cur.next = head
    return head






class Solution:
    def sortedMerge(self,head1, head2):
        ans = Node(0)
        tail = ans 
        while head1 and head2:
            if head1.data < head2.data:
                tail.next = head1 
                head1 = head1.next 
            else:
                tail.next = head2 
                head2 = head2.next 
            tail = tail.next 
        
        if head1:
            tail.next = head1 
        if head2:
            tail.next = head2 
        return ans.next



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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





# Helper to create linked list from list
def createLinkedList(arr):
    head = Node(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = Node(val)
        cur = cur.next
    return head

# Helper to print linked list
def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Example Test
arr = [1, 3, 2, 4, 5]
head = createLinkedList(arr)

M = 3
K = 2

head = addElement(head, M, K)
print("After inserting at position", M, ":")
printList(head)




def insertion(head, K):
    # Create a new node with the given value
    new_node = Node(K)

    # If the list is empty, point new_node to itself and return it as head
    if not head:
        new_node.next = new_node
        return new_node

    # Traverse the list to find the last node
    current = head
    while current.next != head:
        current = current.next

    # Insert the new node at the end
    current.next = new_node
    new_node.next = head

    return head

def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head


class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  
                break
        else:
            return None 
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        if not head or not head.next or k == 0:
            return head 
        # count length 
        temp = head 
        l = 1 
        while temp.next:
            temp = temp.next 
            l += 1 
        k = k % l
        if k == 0:
            return head 
        # go to (k - 1)th node 
        cur = head 
        for _ in range(k - 1):
            cur = cur.next 
        new_head = cur.next 
        cur.next = None 
        temp.next = head 
        return new_head



def check(node,val):
        if node is None:
            return True 
        if node.val != val:
            return False 
        return check(node.left,val) and check(node.right,val)
    return check(root,root.val)


# thinkl for the edge case
