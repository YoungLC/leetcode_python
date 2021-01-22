# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head:
            return []
        if not head.next:
            return [head.val]

        tail = head
        while tail.next is not None:
            tmp = tail.next
            tail.next = tmp.next
            tmp.next = head
            head = tmp

        return print_list_node(head)


def print_list_node(head):
    a = []
    while head:
        a.append(head.val)
        head = head.next
    return a


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(3)
    c = ListNode(2)
    a.next = b
    b.next = c
    c.next = None
    print print_list_node(a)
    print Solution().reversePrint(a)
