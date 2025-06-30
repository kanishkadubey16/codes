
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

# Example Test
arr = [1, 3, 2, 4, 5]
head = createLinkedList(arr)

M = 3
K = 2

head = addElement(head, M, K)
print("After inserting at position", M, ":")
printList(head)



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
