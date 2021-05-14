from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    temp = head
    while L1 and L2:
        if L2.data < L1.data:
            temp.next = L2
            L2 = L2.next
            temp = temp.next
        else:
            temp.next = L1
            L1 = L1.next
            temp = temp.next
    temp.next = L1 or L2
    return head.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
