# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        a = ListNode(None)
        a.next = head
        b = a
        while b.next:
            if b.next.val == val:
                b.next = b.next.next
                return a.next
            else:
                b = b.next


def print_node(h):
    a = []
    while h is not None:
        a.append(h.val)
        h = h.next
    print a


if __name__ == '__main__':
    a = ListNode(4)
    b = ListNode(5)
    c = ListNode(1)
    d = ListNode(9)
    a.next = b
    b.next = c
    c.next = d
    print_node(a)
    val = 5
    print_node(Solution().deleteNode(a, val))
