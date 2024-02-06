
def insert(self,head,data):
    if head is None:
        return Node(data)
    
    tmp = head
    while tmp.next is not None:
        tmp = tmp.next
    tmp.next = Node(data)
    return head
