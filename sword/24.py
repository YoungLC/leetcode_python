# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next is None:
            return head
        tail = head
        while tail.next is not None:
            tmp = tail.next
            tail.next = tmp.next
            tmp.next = head
            head = tmp
        return head


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
    print_node(Solution().reverseList(a))


