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


'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

def deleteAtTail(head):
    if head == None or head.next == None:
        return None 
    prev = None 
    cur = head 

    # move the cur node till last node
    while cur.next != None:
        prev = cur 
        cur = cur.next
    # make second last node next to none
    prev.next = None
    return head





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




'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
'''
def insertnew(head, val , pos):
    new_node = Node(val)
    #edge case
    if pos == 1:
        new_node.next = head
        head.prev = new_node
        return new_node
    #iterate cur to pos-2 steps
    cnt = 1
    cur = head
    while cnt <= pos-2:
            cur = cur.next
            cnt += 1
    #storing the address of the next node before breaking the link
    next_node = cur.next
    #link 4 and 70
    cur.next = new_node
    new_node.prev = cur
    #link 70 and 5
    new_node.next = next_node
    next_node.prev = new_node
    return head


# thinkl for the edge case
