"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    @staticmethod
    def add_two_numbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next

            carry = sum_val // 10
            curr.next = ListNode(sum_val % 10)
            curr = curr.next

        return dummy.next


def convert_linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def run_tests():

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    expected_result = [7, 0, 8]
    result = Solution.add_two_numbers(l1, l2)
    assert convert_linked_list_to_list(result) == expected_result

    l1 = ListNode(0)
    l2 = ListNode(0)
    expected_result = [0]
    result = Solution.add_two_numbers(l1, l2)
    assert convert_linked_list_to_list(result) == expected_result

    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l2 = ListNode(1)
    expected_result = [0, 0, 0, 1]
    result = Solution.add_two_numbers(l1, l2)
    assert convert_linked_list_to_list(result) == expected_result

    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l2 = ListNode(1)
    expected_result = [0, 0, 0, 0, 1]
    result = Solution.add_two_numbers(l1, l2)
    assert convert_linked_list_to_list(result) == expected_result

    l1 = ListNode(1)
    l1.next = ListNode(0)
    l1.next.next = ListNode(0)
    l1.next.next.next = ListNode(0)
    l1.next.next.next.next = ListNode(0)
    l2 = ListNode(2)
    l2.next = ListNode(0)
    l2.next.next = ListNode(0)
    l2.next.next.next = ListNode(0)
    expected_result = [3, 0, 0, 0, 0]
    result = Solution.add_two_numbers(l1, l2)
    assert convert_linked_list_to_list(result) == expected_result

    l1 = ListNode(5)
    l1.next = ListNode(5)
    l2 = ListNode(5)
    l2.next = ListNode(5)
    expected_result = [0, 1, 1]
    result = Solution.add_two_numbers(l1, l2)
    assert convert_linked_list_to_list(result) == expected_result

    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)
    l2.next.next.next.next = ListNode(9)
    expected_result = [8, 9, 9, 9, 9, 1]
    result = Solution.add_two_numbers(l1, l2)
    assert convert_linked_list_to_list(result) == expected_result

    print("Test passed!")


if __name__ == '__main__':
    run_tests()
