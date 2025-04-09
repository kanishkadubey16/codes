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
