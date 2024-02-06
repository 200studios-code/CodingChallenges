
def removeDuplicates(self, head):
    cur = head
    while cur is not None and cur.next is not None:
        nex = cur.next
        while nex is not None and cur.data == nex.data:
            nex = nex.next
        cur.next = nex
        cur = nex
    return head
