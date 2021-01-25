class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        A = ListNode(None)
        B = A
        while l1 and l2:
            if l1.val < l2.val:
                A.next = l1
                l1 = l1.next
                A = A.next
            else:
                A.next = l2
                l2 = l2.next
                A = A.next

        if l1:
            A.next = l1
        if l2:
            A.next = l2
        return B.next


def print_node(h):
    a = []
    while h is not None:
        a.append(h.val)
        h = h.next
    print a


if __name__ == '__main__':
    a1 = ListNode(1)
    b1 = ListNode(3)
    c1 = ListNode(5)
    a1.next = b1
    b1.next = c1
    print_node(a1)

    a2 = ListNode(2)
    b2 = ListNode(4)
    c2 = ListNode(6)
    a2.next = b2
    b2.next = c2
    print_node(a2)

    print_node(Solution().mergeTwoLists(a1, a2))
