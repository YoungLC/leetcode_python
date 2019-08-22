#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
 

Constraints:

The given address is a valid IPv4 address.

'''


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        vetor = []
        for i in address:
            if i == ".":
                vetor.append("[" + i + "]")
            else:
                vetor.append(i)
        return "".join(vetor)


if __name__ == '__main__':
    test_address = "1.1.2.3"
    print Solution().defangIPaddr(test_address)
