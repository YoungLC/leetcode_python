# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l = 0
        tail = head
        while tail:
            l += 1
            tail = tail.next

        for i in range(l-k):
            head = head.next

        return head

def print_list(x):
    a=[]
    while x:
        a.append(x.val)
        x=x.next
    print a


if __name__ == '__main__':
    a=ListNode(1)
    b=ListNode(2)
    c=ListNode(3)
    d=ListNode(4)
    e=ListNode(5)
    a.next=b
    b.next=c
    c.next=d
    d.next=e
    print_list(a)
    print_list(Solution().getKthFromEnd(a,2))

