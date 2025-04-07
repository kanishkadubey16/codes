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
